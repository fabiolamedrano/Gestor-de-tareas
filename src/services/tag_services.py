from fastapi import HTTPException
from starlette import status
from sqlalchemy.orm import Session

from dtos.Tag.tag_create import TagCreateDTO
from dtos.Tag.tag_update import TagUpdateDTO
from models.tag import Tag
from repositories.tag_repository import TagRepository
from repositories.user_repository import UserRepository


class TagService:

    @staticmethod
    def get_tags(user_id: int, db: Session):
        return TagRepository.get_tags(user_id=user_id, db=db)

    @staticmethod
    def find_tag(tag_id: int, db: Session):
        tag = TagRepository.find_tag(tag_id=tag_id, db=db)

        if not tag:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tag not found"
            )

        return tag

    @staticmethod
    def create_tag(dto: TagCreateDTO, db: Session):
        # Check if user exists
        user = UserRepository.find_user(user_id=dto.user_id, db=db)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        # Create data
        data = Tag(
            user_id=dto.user_id,
            name=dto.name
        )

        return TagRepository.create_tag(data=data, db=db)

    @staticmethod
    def update_tag(dto: TagUpdateDTO, db: Session):
        # Create data
        data = Tag(
            id=dto.id,
            name=dto.name
        )

        tag = TagRepository.update_tag(data=data, db=db)

        if not tag:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tag not found"
            )

        return tag

    @staticmethod
    def delete_tag(tag_id: int, db: Session):
        tag = TagRepository.delete_tag(tag_id=tag_id, db=db)

        if not tag:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tag not found"
            )

        return tag