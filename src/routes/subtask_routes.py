from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from config.database import get_db
from models.subtask import Subtask
from dtos.Subtask.subtask_create import SubtaskCreateDTO
from dtos.Subtask.subtask_response import SubtaskResponseDTO
from repositories.subtask_repository import SubtaskRepository
from repositories.task_repository import TaskRepository

router = APIRouter(prefix="/subtasks", tags=["Subtareas"])


@router.get("/task/{task_id}", response_model=list[SubtaskResponseDTO])
def get_subtasks(task_id: int, db: Session = Depends(get_db)):
    """Lista todas las subtareas de una tarea principal."""
    return SubtaskRepository.get_subtasks_by_task(task_id=task_id, db=db)


@router.post("/", response_model=SubtaskResponseDTO, status_code=status.HTTP_201_CREATED)
def create_subtask(data: SubtaskCreateDTO, db: Session = Depends(get_db)):
    """Crea una subtarea asociada a una tarea principal existente."""
    parent_task = TaskRepository.find_task(task_id=data.task_id, db=db)
    if parent_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="La tarea principal no existe"
        )

    subtask = Subtask(
        task_id=data.task_id,
        title=data.title,
        is_completed=False,
    )
    subtask = SubtaskRepository.create_subtask(subtask, db)
    return subtask
