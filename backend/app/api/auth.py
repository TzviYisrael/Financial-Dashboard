# app/api/auth.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import bcrypt

from app.schemas.auth import LoginRequest, LoginResponse
from app.models.user import User
from app.core.database import get_db

# Configuration du router
router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)

@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    """
    Endpoint de connexion utilisateur
    
    Args:
        request: Email et mot de passe
        db: Session de base de données
        
    Returns:
        LoginResponse: Informations utilisateur si succès
        
    Raises:
        HTTPException: 401 si identifiants invalides
    """
    
    # 1. Chercher l'utilisateur par email
    user = db.query(User).filter(User.email == request.email).first()
    
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Email ou mot de passe incorrect"
        )
    
    # 2. Vérifier le mot de passe avec bcrypt directement
    if not bcrypt.checkpw(
        request.password.encode('utf-8'), 
        user.password_hash.encode('utf-8')
    ):
        raise HTTPException(
            status_code=401,
            detail="Email ou mot de passe incorrect"
        )
    
    # 3. Retourner les infos utilisateur
    return LoginResponse(
        id=user.id,
        email=user.email,
        name=user.name,
        message="Connexion réussie"
    )