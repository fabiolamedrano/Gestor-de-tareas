from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Subtask(Base):
    __tablename__ = "Subtasks"

    id = Column(
        "SubtaskID", 
        Integer, 
        primary_key = True, 
        index = True
    )

    title = Column(
        "SubtaskTitle",
        String(250),
        nullable = False
    )

    is_completed = Column(
        "SubtaskIsCompleted",
        Boolean,
        nullable = False,
        default = False
    )

    task_id = Column(
        "TaskId",
        Integer,
        ForeignKey("Task.TaskId"),
        nullable = False
    )

    # Relacion

    task = relationship(
        "Task",
        back_populates = "subtasks"
    )