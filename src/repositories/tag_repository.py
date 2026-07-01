from sqlalchemy.orm import Session
from models.tag import Tag


class TagRepository:

    @staticmethod
    def get_tags(user_id: int, db: Session):
        return db.query(Tag).filter(Tag.user_id == user_id).all()

    @staticmethod
    def find_tag(tag_id: int, db: Session):
        return db.query(Tag).filter(Tag.id == tag_id).first()

    @staticmethod
    def create_tag(data: Tag, db: Session):
        db.add(data)
        db.commit()
        db.refresh(data)
        return data

    @staticmethod
    def update_tag(data: Tag, db: Session):
        tag = TagRepository.find_tag(tag_id=data.id, db=db)

        if tag is None:
            return None

        tag.name = data.name

        db.commit()
        db.refresh(tag)
        return tag

    @staticmethod
    def delete_tag(tag_id: int, db: Session):
        tag = TagRepository.find_tag(tag_id=tag_id, db=db)

        if tag is None:
            return None

        db.delete(tag)
        db.commit()
        return tag