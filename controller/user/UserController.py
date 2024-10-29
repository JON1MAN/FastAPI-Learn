from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from resources.db_configuration import get_db
from service.user.UserService import UserService
from dao.repository.user.UserRepository import UserRepository

user_router = APIRouter()
user_service = UserService(UserRepository())

@user_router.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user(db, user_id)
    return user
