from fastapi import APIRouter, Depends
from starlette import status
from sqlalchemy.orm import Session
from typing import List

from services.tag_services import TagService
from dtos.Tag.tag_create import TagCreateDTO
from dtos.Tag.tag_response import TagResponseDTO
from dtos.Tag.tag_update import TagUpdateDTO
from config.database import get_db

router = APIRouter(
    prefix="/tags",
    tags=["Tags"]
)

@router.get("/user/{user_id}", response_model=List[TagResponseDTO], status_code=status.HTTP_200_OK)
def get_tags(user_id: int, db: Session = Depends(get_db)):
    return TagService.get_tags(user_id=user_id, db=db)

@router.get("/{tag_id}", response_model=TagResponseDTO, status_code=status.HTTP_200_OK)
def find_tag(tag_id: int, db: Session = Depends(get_db)):
    return TagService.find_tag(tag_id=tag_id, db=db)

@router.post("/", response_model=TagResponseDTO, status_code=status.HTTP_201_CREATED)
def create_tag(data: TagCreateDTO, db: Session = Depends(get_db)):
    return TagService.create_tag(dto=data, db=db)

@router.put("/", response_model=TagResponseDTO, status_code=status.HTTP_202_ACCEPTED)
def update_tag(data: TagUpdateDTO, db: Session = Depends(get_db)):
    return TagService.update_tag(dto=data, db=db)

@router.delete("/{tag_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    TagService.delete_tag(tag_id=tag_id, db=db)