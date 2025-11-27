from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from app.core.database import engine, Base, get_db
from app.models import user  # Import user model to register with Base
from sqlalchemy.orm import Session
from app.api import auth
# load the variable 
load_dotenv()


Base.metadata.create_all(bind=engine)

# Create FastAPI
app = FastAPI(
    title=os.getenv("APP_NAME", "Personal Portfolio Copilot API"),
    version=os.getenv("API_VERSION", "v1"),
    description="Backend API for Personal Portfolio Copilot - Educational Investment Platform"
)

#  CORS
origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)

# Endpoints
@app.get("/")
async def root():
    return {
        "message": "Welcome to Personal Portfolio Copilot API",
        "status": "running",
        "version": os.getenv("API_VERSION", "v1"),
        "database": "Supabase Cloud ☁️"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "database": "Supabase - connected",
        "team_member": "David - Backend Developer"
    }

@app.get("/api/test")
async def test_endpoint():
    return {
        "message": "Backend is ready!",
        "cors": "configured",
        "database": "Supabase cloud ready"
    }

@app.get("/api/users/count")
async def count_users(db: Session = Depends(get_db)):
    """
    Count total users in database
    Tests that SQLAlchemy connection works
    """
    from app.models.user import User
    
    count = db.query(User).count()
    
    return {
        "total_users": count,
        "message": "SQLAlchemy connection working!",
        "database": "Supabase PostgreSQL"
    }