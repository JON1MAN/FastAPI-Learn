from sqlalchemy.orm import Session

from service.user.dto.UserSchematic import UserCreate
from dao.repository.user.UserRepository import UserRepository
from dao.model.user.User import User


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, db: Session, user_id: int):
        return self.user_repository.get_user_by_id(db, user_id)

    def get_users(self, db: Session):
        return self.user_repository.get_users(db)

    def create_user(self, db: Session, user_data: UserCreate):
        new_user = User(name=user_data.name,
                        email=user_data.email,
                        password = user_data.password)
        return self.user_repository.create_user(db, new_user)

    def update_user(self, db: Session,
                    user_id: int,
                    user_data: UserCreate):
        user = self.user_repository.get_user_by_id(db, user_id)
        if not user:
            raise ValueError("User not found")

        updated_user = self.user_repository.update_user(db, user_id, user_data)
        return updated_user