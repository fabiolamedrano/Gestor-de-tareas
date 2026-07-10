from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.orm import relationship
from config.database import Base

class Tag(Base):
    __tablename__ = "Tags"

    id = Column(
        "TagId",
        Integer,
        primary_key = True,
        index = True
    )

    name = Column(
        "TagName",
        String(50),
        nullable = False
    )

    user_id = Column(
        "UserId",
        Integer,
        ForeignKey("Users.UserID"),
        nullable = False
    )

    # Relations
    user = relationship(
        "User",
        back_populates = "tags"
    )

    tasks = relationship(
        "Task",
        secondary = "TaskTags",
        back_populates="tags"
    )

