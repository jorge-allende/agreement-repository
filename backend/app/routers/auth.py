from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from passlib.context import CryptContext
from datetime import timedelta
from app.auth.jwt import create_access_token

router = APIRouter()

# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Simulated "database" with a pre-hashed password for testing
fake_users_db = {
    "testuser": {
        "username": "testuser",
        "email": "test@example.com",
        "hashed_password": pwd_context.hash("testpassword")  # Pre-hashed password
    }
}

# Pydantic model for login request
class LoginRequest(BaseModel):
    username: str
    password: str

# Helper function to authenticate user
def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if not user or not pwd_context.verify(password, user["hashed_password"]):
        return None
    return user

# POST /login: Authenticate user and return a JWT token
@router.post("/login")
async def login(request: LoginRequest):
    user = authenticate_user(request.username, request.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    # Generate JWT token
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={"sub": request.username}, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}
