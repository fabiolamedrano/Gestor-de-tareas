from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from config.database import Base


class Task(Base):
    __tablename__ = "Tasks"

    id = Column(
        "TaskId",
        Integer,
        primary_key = True,
        index = True
    )

    title = Column(
        "TaskTitle",
        String(250),
        nullable = False
    )

    description = Column(
        "TaskDescription",
        String(500),
        nullable = True
    )

    priority = Column(
        "TaskPriority",
        String(10),
        nullable = False,
        default = "media"
    )

    status = Column(
        "TaskStatus",
        String(20),
        nullable = False,
        default = "pendiente"
    )

    due_date = Column(
        "TaskDueDate",
        DateTime,
        nullable = True
    )

    progress = Column(
        "TaskProgress",
        Integer,
        nullable = False,
        default = 0
    )

    created_at = Column(
        "TaskCreatedAt",
        DateTime,
        nullable=False
    )

    updated_at = Column(
        "TaskUpdatedAt",
        DateTime,
        nullable=False
    )

    user_id = Column(
        "UserId",
        Integer,
        ForeignKey("Users.UserId"),
        nullable = False
    )

    # Relations
    user = relationship(
        "User",
        back_populates = "tasks"
    )

    tags = relationship(
        "Tag",
        secondary = "TaskTags",
        back_populates = "tasks"
    )

    subtasks = relationship(
        "Subtask",
        back_populates = "task"
    )