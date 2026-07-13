from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session
from typing import List

from services.subtask_services import SubtaskService
from services.task_services import TaskService 
from dtos.Subtask.subtask_create import SubtaskCreateDTO
from dtos.Subtask.subtask_response import SubtaskResponseDTO
from dtos.Subtask.subtask_update import SubtaskUpdateDTO
from config.database import get_db
from config.security import get_current_user 

router = APIRouter(
    prefix="/subtasks",
    tags=["Subtasks"]
)

@router.get("/task/{task_id}", response_model=List[SubtaskResponseDTO], status_code=status.HTTP_200_OK)
def get_subtasks(task_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    task = TaskService.find_task(task_id=task_id, db=db)
    if task.user_id != current_user.get("user_id"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tienes permiso para ver las subtareas de esta tarea")
        
    return SubtaskService.get_subtasks(task_id=task_id, db=db)

@router.get("/{subtask_id}", response_model=SubtaskResponseDTO, status_code=status.HTTP_200_OK)
def find_subtask(subtask_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    subtask = SubtaskService.find_subtask(subtask_id=subtask_id, db=db)
    
    task = TaskService.find_task(task_id=subtask.task_id, db=db)
    if task.user_id != current_user.get("user_id"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tienes permiso para ver esta subtarea")
        
    return subtask

@router.post("/", response_model=SubtaskResponseDTO, status_code=status.HTTP_201_CREATED)
def create_subtask(data: SubtaskCreateDTO, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    task = TaskService.find_task(task_id=data.task_id, db=db)
    if task.user_id != current_user.get("user_id"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tienes permiso para añadir subtareas a esta tarea")
        
    return SubtaskService.create_subtask(dto=data, db=db)

@router.put("/", response_model=SubtaskResponseDTO, status_code=status.HTTP_202_ACCEPTED)
def update_subtask(data: SubtaskUpdateDTO, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    subtask = SubtaskService.find_subtask(subtask_id=data.id, db=db)
    
    task = TaskService.find_task(task_id=subtask.task_id, db=db)
    if task.user_id != current_user.get("user_id"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tienes permiso para modificar esta subtarea")
        
    return SubtaskService.update_subtask(dto=data, db=db)

@router.delete("/{subtask_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_subtask(subtask_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    subtask = SubtaskService.find_subtask(subtask_id=subtask_id, db=db)
    
    task = TaskService.find_task(task_id=subtask.task_id, db=db)
    if task.user_id != current_user.get("user_id"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tienes permiso para eliminar esta subtarea")
        
    SubtaskService.delete_subtask(subtask_id=subtask_id, db=db)
    