from fastapi import HTTPException
from starlette import status
from sqlalchemy.orm import Session

from datetime import datetime, timezone

from dtos.Task.task_create import TaskCreateDTO
from dtos.Task.task_update import TaskUpdateDTO
from models.task import Task
from models.tag import Tag
from repositories.task_repository import TaskRepository
from repositories.user_repository import UserRepository
from repositories.tag_repository import TagRepository


class TaskService:

    @staticmethod
    def _resolve_tags(user_id: int, tag_names: list, db: Session):
        """Busca cada etiqueta por nombre; si no existe, la crea."""
        tags = []
        for raw_name in tag_names:
            name = raw_name.strip()
            if not name:
                continue
            tag = TagRepository.find_tag_by_name(user_id=user_id, name=name, db=db)
            if not tag:
                tag = TagRepository.create_tag(data=Tag(user_id=user_id, name=name), db=db)
            tags.append(tag)
        return tags

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

        task = TaskRepository.create_task(data=data, db=db)

        # Asignar etiquetas (crear las que no existan)
        if dto.tag_names:
            task.tags = TaskService._resolve_tags(user_id=dto.user_id, tag_names=dto.tag_names, db=db)
            db.commit()
            db.refresh(task)

        return task

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

        updated_task = TaskRepository.update_task(data=data, db=db)

        # Actualizar etiquetas (reemplaza las asignaciones actuales)
        if dto.tag_names is not None:
            updated_task.tags = TaskService._resolve_tags(user_id=task.user_id, tag_names=dto.tag_names, db=db)
            db.commit()
            db.refresh(updated_task)

        return updated_task

    @staticmethod
    def delete_task(task_id: int, db: Session):
        task = TaskRepository.delete_task(task_id=task_id, db=db)

        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        return task