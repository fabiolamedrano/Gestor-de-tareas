from sqlalchemy.orm import Session
from models.subtask import Subtask


class SubtaskRepository:

    @staticmethod
    def get_subtasks_by_task(task_id: int, db: Session):
        return db.query(Subtask).filter(Subtask.task_id == task_id).all()

    @staticmethod
    def create_subtask(data: Subtask, db: Session):
        db.add(data)
        db.commit()
        db.refresh(data)
        return data
