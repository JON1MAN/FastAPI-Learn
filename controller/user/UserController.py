from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from service.user.dto.UserSchematic import UserResponse, UserCreate
from resources.db_configuration import get_db
from service.user.UserService import UserService
from dao.repository.user.UserRepository import UserRepository

from typing import List

user_router = APIRouter()
user_service = UserService(UserRepository())

@user_router.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user(db, user_id)
    return user

@user_router.get("/users", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)

@user_router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)

@user_router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserCreate,
                db: Session = Depends(get_db)):
    try:
        updated_user = user_service.update_user(db, user_id, user)
        return updated_user
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))