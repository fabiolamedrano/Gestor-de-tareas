from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session
from typing import List

from services.task_services import TaskService
from dtos.Task.task_create import TaskCreateDTO
from dtos.Task.task_response import TaskResponseDTO
from dtos.Task.task_update import TaskUpdateDTO
from config.database import get_db
from config.security import get_current_user 

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.get("/", response_model=List[TaskResponseDTO], status_code=status.HTTP_200_OK)
def get_tasks(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    user_id = current_user.get("user_id")
    return TaskService.get_tasks(user_id=user_id, db=db)

@router.get("/{task_id}", response_model=TaskResponseDTO, status_code=status.HTTP_200_OK)
def find_task(task_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    task = TaskService.find_task(task_id=task_id, db=db)
    
    if task.user_id != current_user.get("user_id"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tienes permiso para ver esta tarea")
        
    return task

@router.post("/", response_model=TaskResponseDTO, status_code=status.HTTP_201_CREATED)
def create_task(data: TaskCreateDTO, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    data.user_id = current_user.get("user_id") 
    return TaskService.create_task(dto=data, db=db)

@router.put("/", response_model=TaskResponseDTO, status_code=status.HTTP_202_ACCEPTED)
def update_task(data: TaskUpdateDTO, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    task = TaskService.find_task(task_id=data.id, db=db)
    if task.user_id != current_user.get("user_id"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tienes permiso para actualizar esta tarea")
        
    return TaskService.update_task(dto=data, db=db)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    task = TaskService.find_task(task_id=task_id, db=db)
    
    if task.user_id != current_user.get("user_id"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tienes permiso para eliminar esta tarea")
        
    TaskService.delete_task(task_id=task_id, db=db)
