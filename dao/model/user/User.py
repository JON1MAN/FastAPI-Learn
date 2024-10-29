from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from resources.db_configuration import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    email = Column(String(100), unique=True ,index=True)
    password = Column(String(100))