from pydantic import BaseModel, ConfigDict


class SubtaskResponseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    task_id: int
    title: str
    is_completed: bool
