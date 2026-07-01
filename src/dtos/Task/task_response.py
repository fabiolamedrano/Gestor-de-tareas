from pydantic import BaseModel
from datetime import datetime

class TaskResponseDTO(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    priority: str
    status: str
    due_date: datetime
    created_at: datetime
    updated_at: datetime