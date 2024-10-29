from sqlalchemy.orm import Session
from dao.repository.user.UserRepository import UserRepository
from dao.model.user import User

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, db:Session, user_id: int):
        return self.user_repository.get_user_by_id(db, user_id)