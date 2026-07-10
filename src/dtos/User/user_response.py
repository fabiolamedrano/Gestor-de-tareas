from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserResponseDTO(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime