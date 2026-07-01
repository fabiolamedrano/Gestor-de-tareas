from pydantic import BaseModel

class TagResponseDTO(BaseModel):
    id: int
    user_id: int
    name: str