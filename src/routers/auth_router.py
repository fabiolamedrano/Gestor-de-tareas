from fastapi import APIRouter, Depends
from starlette import status
from sqlalchemy.orm import Session

from services.auth_service import AuthService
from dtos.Auth.auth_login import AuthLoginDTO
from dtos.Auth.auth_response import AuthResponseDTO
from config.database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/login", response_model=AuthResponseDTO, status_code=status.HTTP_200_OK)
def login(data: AuthLoginDTO, db: Session = Depends(get_db)):
    return AuthService.login(dto=data, db=db)