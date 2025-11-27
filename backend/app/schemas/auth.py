from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    """ scheme for login request"""
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    """Schéma for login response"""
    id: int
    email: str
    name: str
    message: str

    class Config:
        from_attributes = True