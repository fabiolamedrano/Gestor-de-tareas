from pydantic import BaseModel, EmailStr


class AuthLoginDTO(BaseModel):
    email: EmailStr
    password: str