from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.sql.annotation import Annotated

from dao.repository.user.UserRepository import UserRepository

auth = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class CurrentUser(BaseModel):
    name: str
    email: str
    disabled: bool

def decode_token(token):
    return CurrentUser(
        name=token+"decoded"
    )

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = decode_token(token)
    return user

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(db, username: str, password: str):
    user = UserRepository.get_user_by_email(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


@auth.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token" : token}

@auth.get("/users/me")
async def read_items(current_user: Annotated[CurrentUser, Depends(get_current_user)]):
    return current_user

