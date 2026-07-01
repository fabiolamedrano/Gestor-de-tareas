from pydantic import BaseModel, Field
from datetime import datetime

class TaskCreateDTO(BaseModel):
    user_id: int
    title: str = Field(min_length=1, max_length=250)
    description: str = Field(default=None, max_length=500)
    priority: str = Field(default="media")
    due_date: datetime = None