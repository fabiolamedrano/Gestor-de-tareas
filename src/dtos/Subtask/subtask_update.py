from pydantic import BaseModel, Field


class SubtaskUpdateDTO(BaseModel):
    id: int
    title: str = Field(min_length=1, max_length=250)
    is_completed: bool