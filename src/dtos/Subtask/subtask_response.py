from pydantic import BaseModel


class SubtaskResponseDTO(BaseModel):
    id: int
    task_id: int
    title: str
    is_completed: bool