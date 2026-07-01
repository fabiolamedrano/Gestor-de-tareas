from pydantic import BaseModel, Field
from datetime import datetime

class TaskUpdateDTO(BaseModel):
    id: int
    title: str = Field(min_length=1, max_length=250)
    description: str = Field(default=None, max_length=500)
    priority: str
    status: str
    due_date: datetime = None