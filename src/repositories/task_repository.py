from sqlalchemy.orm import Session, joinedload
from models.task import Task


class TaskRepository:

    @staticmethod
    def get_tasks(user_id: int, db: Session):
        return db.query(Task).options(
            joinedload(Task.subtasks),
            joinedload(Task.tags)
        ).filter(Task.user_id == user_id).all()

    @staticmethod
    def find_task(task_id: int, db: Session):
        return db.query(Task).options(
            joinedload(Task.subtasks),
            joinedload(Task.tags)
        ).filter(Task.id == task_id).first()

    @staticmethod
    def create_task(data: Task, db: Session):
        db.add(data)
        db.commit()
        db.refresh(data)
        return data

    @staticmethod
    def update_task(data: Task, db: Session):
        task = TaskRepository.find_task(task_id=data.id, db=db)

        if task is None:
            return None

        task.title = data.title
        task.description = data.description
        task.priority = data.priority
        task.status = data.status
        task.due_date = data.due_date
        task.progress = data.progress
        task.updated_at = data.updated_at

        db.commit()
        db.refresh(task)
        return task

    @staticmethod
    def delete_task(task_id: int, db: Session):
        task = TaskRepository.find_task(task_id=task_id, db=db)

        if task is None:
            return None

        db.delete(task)
        db.commit()
        return task