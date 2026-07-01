from pydantic import BaseModel, EmailStr, Field

class UserCreateDTO(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)