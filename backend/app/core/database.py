from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")

# Create SQLAlchemy engine
# - connect_args with check_same_thread is for SQLite (not needed for PostgreSQL but doesn't hurt)
# - echo=True logs all SQL queries (useful for debugging, set to False in production)
engine = create_engine(
    DATABASE_URL,
    echo=False  # Set to True to see SQL queries in console
)


# Create SessionLocal class
# - Each instance of SessionLocal is a database session
# - autocommit=False means you must explicitly call commit() to save changes
# - autoflush=False means changes aren't automatically flushed to DB
# - bind=engine connects the session to our database engine
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Create Base class for declarative models
# - All models (User, Portfolio, etc.) will inherit from this Base
# - Base tracks all model classes and their table definitions
Base = declarative_base()

# Dependency function to get database session
# - Used with FastAPI's Depends() to inject DB session into routes
# - Ensures the session is always closed after request (with try/finally)
def get_db():
    """
    Get database session for dependency injection
    
    Usage in FastAPI route:
    @app.get("/users")
    def get_users(db: Session = Depends(get_db)):
        users = db.query(User).all()
        return users
    """
    db = SessionLocal()
    try:
        yield db  # Provide session to route
    finally:
        db.close()  # Always close session after request