"""
User model - Represents users table in database
Stores user authentication and profile information
"""

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base


class User(Base):
    """
    User model for authentication and profile
    
    Attributes:
        id: Primary key, auto-incremented
        email: Unique email address for login
        password_hash: Hashed password (never store plain text!)
        name: User's full name (optional)
        created_at: Timestamp of account creation (auto-generated)
    """
    
    # Table name in PostgreSQL
    __tablename__ = "users"
    
    # Primary key - auto-incremented integer
    id = Column(
        Integer,
        primary_key=True,  # This is the primary key
        index=True,        # Create index for faster lookups
        autoincrement=True # Automatically increment for each new user
    )
    
    # Email - unique and required
    email = Column(
        String,
        unique=True,       # No two users can have same email
        index=True,        # Create index for faster email lookups
        nullable=False     # Email is required (cannot be NULL)
    )
    
    # Password hash - never store plain text passwords!
    # We'll hash passwords with bcrypt before storing
    password_hash = Column(
        String,
        nullable=False     # Password is required
    )
    
    # User's full name - optional
    name = Column(
        String,
        nullable=True      # Name is optional (can be NULL)
    )
    
    # Timestamp of account creation
    # Uses PostgreSQL's CURRENT_TIMESTAMP by default
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),  # Auto-set to current time on creation
        nullable=False
    )
    
    def __repr__(self):
        """
        String representation of User object
        Useful for debugging and logging
        """
        return f"<User(id={self.id}, email='{self.email}', name='{self.name}')>"