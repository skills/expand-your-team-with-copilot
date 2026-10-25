"""
Authentication endpoints for the High School Management System API
"""

from fastapi import APIRouter, HTTPException
from typing import Dict, Any
import hashlib
import secrets

from ..database import teachers_collection

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

# Maps server-issued session tokens to the username they were issued for.
# A token is only added here after /login verifies the account password,
# so possession of a valid token is proof of a successful authentication.
active_sessions: Dict[str, str] = {}

def hash_password(password):
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

@router.post("/login")
def login(username: str, password: str) -> Dict[str, Any]:
    """Login a teacher account"""
    # Hash the provided password
    hashed_password = hash_password(password)
    
    # Find the teacher in the database
    teacher = teachers_collection.find_one({"_id": username})
    
    if not teacher or teacher["password"] != hashed_password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    # Issue a server-generated session token proving this login was authenticated
    session_token = secrets.token_urlsafe(32)
    active_sessions[session_token] = username
    
    # Return teacher information (excluding password)
    return {
        "username": teacher["username"],
        "display_name": teacher["display_name"],
        "role": teacher["role"],
        "session_token": session_token
    }

@router.get("/check-session")
def check_session(username: str, session_token: str) -> Dict[str, Any]:
    """Check if a session is valid using a server-issued session token"""
    if active_sessions.get(session_token) != username:
        raise HTTPException(status_code=401, detail="Invalid or expired session")
    
    teacher = teachers_collection.find_one({"_id": username})
    
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    
    return {
        "username": teacher["username"],
        "display_name": teacher["display_name"],
        "role": teacher["role"]
    }