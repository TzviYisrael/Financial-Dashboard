from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# load the variable 
load_dotenv()

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
