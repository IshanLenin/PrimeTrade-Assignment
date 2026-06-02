from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import database, models, schemas
from ..database import get_db
from ..config import get_current_user

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.post("", response_model=schemas.TaskResponse)
def create_task(
    task: schemas.TaskCreate, 
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    # Automatically link the new task to the user who created it
    new_task = models.Task(
        title=task.title, 
        description=task.description, 
        owner_id=current_user.id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("", response_model=List[schemas.TaskResponse])
def read_tasks(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    # Fetch only the tasks belonging to the logged-in user
    tasks = db.query(models.Task).filter(models.Task.owner_id == current_user.id).all()
    return tasks

@router.patch("/{task_id}", response_model=schemas.TaskResponse)
def update_task(task_id: int, task_update: schemas.TaskUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):

    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    if task.owner_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized to assign tasks")

    task.title = task_update.title
    task.description = task_update.description

    db.commit()
    db.refresh(task)
    return task

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    # Find the task
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # ROLE-BASED CHECK: Are they the owner OR an admin?
    if task.owner_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized to delete this task")
    
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}