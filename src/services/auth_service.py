from fastapi import HTTPException
from starlette import status
from sqlalchemy.orm import Session

from dtos.Auth.auth_login import AuthLoginDTO
from repositories.user_repository import UserRepository
from config.security import verify_password, create_access_token


class AuthService:

    @staticmethod
    def login(dto: AuthLoginDTO, db: Session):
        # Check if user exists
        user = UserRepository.find_user_by_email(email=dto.email, db=db)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Correo o contraseña incorrectos"
            )

        # Verify password
        if not verify_password(dto.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Correo o contraseña incorrectos"
            )

        # Create token
        token = create_access_token(data={"sub": user.email, "user_id": user.id})

        return {
            "access_token": token,
            "token_type": "bearer",
            "user_id": user.id,
            "email": user.email
        }