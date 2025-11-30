"""
Authentication schemas for request/response validation
"""

from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    """Schema for login request"""
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    """Schema for user information in responses"""
    id: int
    email: str
    name: str
    
    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    """Schema for authentication token response"""
    access_token: str
    token_type: str
    user: UserResponse
