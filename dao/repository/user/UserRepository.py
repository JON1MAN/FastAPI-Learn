from typing import Optional, List

from sqlalchemy.orm import Session
from dao.model.user.User import User


class UserRepository:
    def get_user_by_id(self, db: Session, user_id: int) :
        return db.query(User).filter(User.id == user_id).first()

    def get_users(self, db: Session):
        return db.query(User).all()

    def create_user(self, db: Session, user: User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
