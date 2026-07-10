from fastapi import APIRouter, Depends
from starlette import status
from sqlalchemy.orm import Session
from typing import List

from services.subtask_services import SubtaskService
from dtos.Subtask.subtask_create import SubtaskCreateDTO
from dtos.Subtask.subtask_response import SubtaskResponseDTO
from dtos.Subtask.subtask_update import SubtaskUpdateDTO
from config.database import get_db

router = APIRouter(
    prefix="/subtasks",
    tags=["Subtasks"]
)

@router.get("/task/{task_id}", response_model=List[SubtaskResponseDTO], status_code=status.HTTP_200_OK)
def get_subtasks(task_id: int, db: Session = Depends(get_db)):
    return SubtaskService.get_subtasks(task_id=task_id, db=db)

@router.get("/{subtask_id}", response_model=SubtaskResponseDTO, status_code=status.HTTP_200_OK)
def find_subtask(subtask_id: int, db: Session = Depends(get_db)):
    return SubtaskService.find_subtask(subtask_id=subtask_id, db=db)

@router.post("/", response_model=SubtaskResponseDTO, status_code=status.HTTP_201_CREATED)
def create_subtask(data: SubtaskCreateDTO, db: Session = Depends(get_db)):
    return SubtaskService.create_subtask(dto=data, db=db)

@router.put("/", response_model=SubtaskResponseDTO, status_code=status.HTTP_202_ACCEPTED)
def update_subtask(data: SubtaskUpdateDTO, db: Session = Depends(get_db)):
    return SubtaskService.update_subtask(dto=data, db=db)

@router.delete("/{subtask_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_subtask(subtask_id: int, db: Session = Depends(get_db)):
    SubtaskService.delete_subtask(subtask_id=subtask_id, db=db)