from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Table
)
from config.database import Base


TaskTag = Table(
    "TaskTags",
    Base.metadata,
    Column(
        "TaskId",
        Integer,
        ForeignKey("Tasks.TaskId"),
        primary_key = True
    ),
    Column(
        "TagId",
        Integer,
        ForeignKey("Tags.TagId"),
        primary_key = True
    )
)