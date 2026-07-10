from sqlalchemy.orm import Session
from models.subtask import Subtask


class SubtaskRepository:

    @staticmethod
    def get_subtasks_by_task(task_id: int, db: Session):
        return db.query(Subtask).filter(Subtask.task_id == task_id).all()

    @staticmethod
    def find_subtask(subtask_id: int, db: Session):
        return db.query(Subtask).filter(Subtask.id == subtask_id).first()

    @staticmethod
    def create_subtask(data: Subtask, db: Session):
        db.add(data)
        db.commit()
        db.refresh(data)
        return data

    @staticmethod
    def update_subtask(data: Subtask, db: Session):
        subtask = SubtaskRepository.find_subtask(subtask_id=data.id, db=db)

        if subtask is None:
            return None

        subtask.title = data.title
        subtask.is_completed = data.is_completed

        db.commit()
        db.refresh(subtask)
        return subtask

    @staticmethod
    def delete_subtask(subtask_id: int, db: Session):
        subtask = SubtaskRepository.find_subtask(subtask_id=subtask_id, db=db)

        if subtask is None:
            return None

        db.delete(subtask)
        db.commit()
        return subtask