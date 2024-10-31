from sqlalchemy.orm import Session
from dao.model.user.User import User
from service.user.dto.UserSchematic import UserCreate


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

    def update_user(self, db: Session,
                    user_id: int,
                    user_data: UserCreate):
        user = self.get_user_by_id(db, user_id)

        if not user:
            raise ValueError("User not found")

        if user_data.name:
            user.name = user_data.name
        if user_data.email:
            user.email = user_data.email
        if user_data.password:
            user.password = user_data.password

        db.commit()
        db.refresh(user)

        return user