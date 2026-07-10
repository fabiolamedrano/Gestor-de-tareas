from pydantic import BaseModel, EmailStr, Field


class UserUpdateDTO(BaseModel):
    id: int
    email: EmailStr
    password: str = Field(min_length=8)