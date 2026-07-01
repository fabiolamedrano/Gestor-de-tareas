from sqlalchemy.orm import Session
from models.user import User


class UserRepository:

    @staticmethod
    def get_users(db: Session):
        return db.query(User).all()

    @staticmethod
    def find_user(user_id: int, db: Session):
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def find_user_by_email(email: str, db: Session):
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def create_user(data: User, db: Session):
        db.add(data)
        db.commit()
        db.refresh(data)
        return data

    @staticmethod
    def update_user(data: User, db: Session):
        user = UserRepository.find_user(user_id=data.id, db=db)

        if user is None:
            return None

        user.email = data.email
        user.password = data.password

        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def delete_user(user_id: int, db: Session):
        user = UserRepository.find_user(user_id=user_id, db=db)

        if user is None:
            return None

        db.delete(user)
        db.commit()
        return user