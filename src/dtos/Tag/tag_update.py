from pydantic import BaseModel, Field

class TagUpdateDTO(BaseModel):
    id: int
    name: str = Field(min_length=1, max_length=50)