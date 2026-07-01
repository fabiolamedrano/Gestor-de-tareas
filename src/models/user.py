from sqlalchemy import (
    Column,
    Integer,
    String,
    Datetime
)

from sqlalchemy.orm import relationship
from config.database import Base

class User(Base):
    __tablename__ = "Users"

    id = Column(
        "UserID",
        Integer,
        primary_key = True,
        index = True
    )

    email = Column(
        "UserEmail",
        String(100),
        nullable = False,
        unique = True
    )

    password = Column(
        "UserPassword",
        String(255),
        nullable = False
    )

    created_at = Column(
        "UserCreatedAt",
        Datetime,
        nullable = False
    )

    task = relationship(
        "Task",
        back_populates = "user"
    )

    tags = relationship(
        "Tag",
        back_populates = "user"
    )