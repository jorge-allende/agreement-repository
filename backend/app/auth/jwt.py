from datetime import datetime, timedelta, timezone
from jose import jwt
import os

SECRET_KEY = os.getenv("SECRET_KEY", "dev-placeholder-secret-key")
ALOGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALOGORITHM)
    return encoded_jwt