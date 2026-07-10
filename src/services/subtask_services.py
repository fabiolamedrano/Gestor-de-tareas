from fastapi import HTTPException
from starlette import status
from sqlalchemy.orm import Session

from dtos.Subtask.subtask_create import SubtaskCreateDTO
from dtos.Subtask.subtask_update import SubtaskUpdateDTO
from models.subtask import Subtask
from repositories.subtask_repository import SubtaskRepository
from repositories.task_repository import TaskRepository

class SubtaskService:

    @staticmethod
    def get_subtasks(task_id: int, db: Session):
        return SubtaskRepository.get_subtasks_by_task(task_id=task_id, db=db)

    @staticmethod
    def find_subtask(subtask_id: int, db: Session):
        subtask = SubtaskRepository.find_subtask(subtask_id=subtask_id, db=db)

        if not subtask:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Subtask not found"
            )

        return subtask

    @staticmethod
    def create_subtask(dto: SubtaskCreateDTO, db: Session):
        # Check if parent task exists
        task = TaskRepository.find_task(task_id=dto.task_id, db=db)

        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="La tarea principal no existe"
            )

        # Create data
        data = Subtask(
            task_id=dto.task_id,
            title=dto.title,
            is_completed=False
        )

        return SubtaskRepository.create_subtask(data=data, db=db)

    @staticmethod
    def update_subtask(dto: SubtaskUpdateDTO, db: Session):
        data = Subtask(
            id=dto.id,
            title=dto.title,
            is_completed=dto.is_completed
        )

        subtask = SubtaskRepository.update_subtask(data=data, db=db)

        if not subtask:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Subtask not found"
            )

        task = TaskRepository.find_task(task_id=subtask.task_id, db=db)
        if task:
            total = len(task.subtasks)
            completed = sum(1 for s in task.subtasks if s.is_completed)
            task.progress = int((completed / total) * 100) if total > 0 else 0
            db.commit()

        return subtask

    @staticmethod
    def delete_subtask(subtask_id: int, db: Session):
        subtask = SubtaskRepository.delete_subtask(subtask_id=subtask_id, db=db)

        if not subtask:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Subtask not found"
            )

        return subtask