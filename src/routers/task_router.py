from fastapi import APIRouter, Depends
from starlette import status
from sqlalchemy.orm import Session
from typing import List

from services.task_services import TaskService
from dtos.Task.task_create import TaskCreateDTO
from dtos.Task.task_response import TaskResponseDTO
from dtos.Task.task_update import TaskUpdateDTO
from config.database import get_db

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.get("/user/{user_id}", response_model=List[TaskResponseDTO], status_code=status.HTTP_200_OK)
def get_tasks(user_id: int, db: Session = Depends(get_db)):
    return TaskService.get_tasks(user_id=user_id, db=db)

@router.get("/{task_id}", response_model=TaskResponseDTO, status_code=status.HTTP_200_OK)
def find_task(task_id: int, db: Session = Depends(get_db)):
    return TaskService.find_task(task_id=task_id, db=db)

@router.post("/", response_model=TaskResponseDTO, status_code=status.HTTP_201_CREATED)
def create_task(data: TaskCreateDTO, db: Session = Depends(get_db)):
    return TaskService.create_task(dto=data, db=db)

@router.put("/", response_model=TaskResponseDTO, status_code=status.HTTP_202_ACCEPTED)
def update_task(data: TaskUpdateDTO, db: Session = Depends(get_db)):
    return TaskService.update_task(dto=data, db=db)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    TaskService.delete_task(task_id=task_id, db=db)