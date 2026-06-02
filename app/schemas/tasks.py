from pydantic import BaseModel, Field
from typing import Optional

# --- Task Schemas ---
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

class TaskCreate(TaskBase):
    task_id: Optional[int] = None
    description: str = Field(min_length=1)
    owner_id: Optional[int] = None

class TaskResponse(TaskBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True  # Allows Pydantic to read SQLAlchemy models

class TaskUpdate(TaskBase):
    title: Optional[str]
    description: Optional[str]
    
    class Config:
        from_attributes = True
