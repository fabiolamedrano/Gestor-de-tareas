from pydantic import BaseModel
from datetime import datetime
from typing import List

from dtos.Tag.tag_response import TagResponseDTO
from dtos.Subtask.subtask_response import SubtaskResponseDTO


class TaskResponseDTO(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    priority: str
    status: str
    progress: int
    due_date: datetime
    created_at: datetime
    updated_at: datetime
    tags: List[TagResponseDTO] = []
    subtasks: List[SubtaskResponseDTO] = []