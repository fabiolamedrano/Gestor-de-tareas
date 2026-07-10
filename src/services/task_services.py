from fastapi import HTTPException
from starlette import status
from sqlalchemy.orm import Session

from datetime import datetime, timezone

from dtos.Task.task_create import TaskCreateDTO
from dtos.Task.task_update import TaskUpdateDTO
from models.task import Task
from repositories.task_repository import TaskRepository
from repositories.user_repository import UserRepository


class TaskService:

    @staticmethod
    def get_tasks(user_id: int, db: Session):
        return TaskRepository.get_tasks(user_id=user_id, db=db)

    @staticmethod
    def find_task(task_id: int, db: Session):
        task = TaskRepository.find_task(task_id=task_id, db=db)

        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        return task

    @staticmethod
    def create_task(dto: TaskCreateDTO, db: Session):
        # Check if user exists
        user = UserRepository.find_user(user_id=dto.user_id, db=db)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        # Create data
        data = Task(
            user_id=dto.user_id,
            title=dto.title,
            description=dto.description,
            priority=dto.priority,
            status="pendiente",
            progress=0,
            due_date=dto.due_date,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )

        return TaskRepository.create_task(data=data, db=db)

    @staticmethod
    def update_task(dto: TaskUpdateDTO, db: Session):
        # Check if task exists
        task = TaskRepository.find_task(task_id=dto.id, db=db)

        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        # Calculate progress based on subtasks
        total = len(task.subtasks)
        if total == 0:
            progress = 0
        else:
            completed = sum(1 for s in task.subtasks if s.is_completed)
            progress = int((completed / total) * 100)

        # Create data
        data = Task(
            id=dto.id,
            title=dto.title,
            description=dto.description,
            priority=dto.priority,
            status=dto.status,
            due_date=dto.due_date,
            progress=progress,
            updated_at=datetime.now(timezone.utc)
        )

        return TaskRepository.update_task(data=data, db=db)

    @staticmethod
    def delete_task(task_id: int, db: Session):
        task = TaskRepository.delete_task(task_id=task_id, db=db)

        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        return task
    
    @staticmethod
    def recalculate_progress(task_id: int, db: Session):
        task = TaskRepository.find_task(task_id=task_id, db=db)

        if not task:
            return

        total = len(task.subtasks)
        if total == 0:
            progress = 0
        else:
            completed = sum(1 for s in task.subtasks if s.is_completed)
            progress = int((completed / total) * 100)

        task.progress = progress
        db.commit()
        db.refresh(task)