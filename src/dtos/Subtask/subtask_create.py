from pydantic import BaseModel, Field


class SubtaskCreateDTO(BaseModel):
    task_id: int
    title: str = Field(min_length=1, max_length=250)
