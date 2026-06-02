from pydantic import BaseModel, EmailStr, Field
from typing import Optional
# --- User Schemas ---
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)
    #bcrypt only accepts upto 72 bytes of string

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role: str 

    class Config:
        from_attributes = True

# --- Auth Schemas ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
