from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class UserUpdateDTO(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime