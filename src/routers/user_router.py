from fastapi import APIRouter, Depends
from starlette import status
from sqlalchemy.orm import Session
from typing import List

from services.user_services import UserService
from dtos.User.user_create import UserCreateDTO
from dtos.User.user_response import UserResponseDTO
from dtos.User.user_update import UserUpdateDTO
from config.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/", response_model=List[UserResponseDTO], status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    return UserService.get_users(db=db)

@router.get("/{user_id}", response_model=UserResponseDTO, status_code=status.HTTP_200_OK)
def find_user(user_id: int, db: Session = Depends(get_db)):
    return UserService.find_user(user_id=user_id, db=db)

@router.post("/", response_model=UserResponseDTO, status_code=status.HTTP_201_CREATED)
def create_user(data: UserCreateDTO, db: Session = Depends(get_db)):
    return UserService.create_user(dto=data, db=db)

@router.put("/", response_model=UserResponseDTO, status_code=status.HTTP_202_ACCEPTED)
def update_user(data: UserUpdateDTO, db: Session = Depends(get_db)):
    return UserService.update_user(dto=data, db=db)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    UserService.delete_user(user_id=user_id, db=db)