from fastapi import HTTPException
from starlette import status
from sqlalchemy.orm import Session

from datetime import datetime, timezone

from dtos.User.user_create import UserCreateDTO
from dtos.User.user_update import UserUpdateDTO
from models.user import User
from repositories.user_repository import UserRepository
from config.security import hash_password

class UserService:

    @staticmethod
    def get_users(db: Session):
        return UserRepository.get_users(db=db)

    @staticmethod
    def find_user(user_id: int, db: Session):
        user = UserRepository.find_user(user_id=user_id, db=db)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return user

    @staticmethod
    def create_user(dto: UserCreateDTO, db: Session):
        # Check if email already exists
        existing = UserRepository.find_user_by_email(email=dto.email, db=db)

        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Este correo ya está en uso"
            )

        # Create data
        data = User(
            email=dto.email,
            password=hash_password(dto.password),
            created_at=datetime.now(timezone.utc)
        )

        return UserRepository.create_user(data=data, db=db)

    @staticmethod
    def update_user(dto: UserUpdateDTO, db: Session):
        # Check if email already exists
        existing = UserRepository.find_user_by_email(email=dto.email, db=db)

        if existing and existing.id != dto.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Este correo ya está en uso"
            )

        # Create data
        data = User(
            id=dto.id,
            email=dto.email,
            password=hash_password(dto.password)
        )

        user = UserRepository.update_user(data=data, db=db)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return user

    @staticmethod
    def delete_user(user_id: int, db: Session):
        user = UserRepository.delete_user(user_id=user_id, db=db)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return user