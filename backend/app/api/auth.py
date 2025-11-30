"""
Authentication API endpoints
"""

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
import bcrypt

from app.schemas.auth import LoginRequest, TokenResponse, UserResponse
from app.models.user import User
from app.core.database import get_db
from app.utils.jwt import create_access_token

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)


@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    """
    User login endpoint
    Authenticates user and returns JWT token
    """
    
    # Find user by email
    user = db.query(User).filter(User.email == request.email).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou mot de passe incorrect"
        )
    
    # Verify password
    if not bcrypt.checkpw(
        request.password.encode('utf-8'), 
        user.password_hash.encode('utf-8')
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou mot de passe incorrect"
        )
    
    # Create JWT token
    access_token = create_access_token(
        data={
            "user_id": user.id,
            "email": user.email
        }
    )
    
    # Return token and user info
    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        user=UserResponse(
            id=user.id,
            email=user.email,
            name=user.name
        )
    )
