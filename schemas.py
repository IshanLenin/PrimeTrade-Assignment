from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# --- Task Schemas ---
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True  # Allows Pydantic to read SQLAlchemy models

# --- User Schemas ---
class UserCreate(BaseModel):
    name:str
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)
    #bcrypt only accepts upto 72 bytes of string

class UserResponse(BaseModel):
    id: int
    name:str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True

# --- Auth Schemas ---
class Token(BaseModel):
    access_token: str
    token_type: str