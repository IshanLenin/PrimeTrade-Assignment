from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from .schemas import users as user_schemas
from .models import users as user_models
from .database import get_db

# These must be stored in a .env file, but for the sake of the assessment I have included them in the main file.
SECRET_KEY = "password@123" 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") 
#deprecated means if a password that was hashed with a previous version is given, it will still be verified and updated to the latest version
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Decode the token payload
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        print(f"--- THE DECODED PAYLOAD IS: {payload} ---") # <--- ADD THIS
        
        email: str = payload.get("sub")
        if email is None:
            print("--- CRASH: COULD NOT FIND 'sub' ---") # <--- ADD THIS
            raise credentials_exception
        print(f"--- THE EMAIL IS: {email} ---")
        
        token_data = user_schemas.TokenData(email=email) 
        
    except JWTError as e:
        print(f"--- JWT ERROR CRASH: {e} ---") # <--- ADD THIS
        raise credentials_exception

    # 3. Query your database using your explicit SQLAlchemy Table namespace
    current_user = db.query(user_models.User).filter(user_models.User.email == token_data.email).first()
    
    if current_user is None:
        raise credentials_exception
        
    # 4. Return the database user record object smoothly
    return current_user

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    # Sign the token with our secret key
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt