from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base

from schema.my_enum import RoleUser

Base = declarative_base()


class UserTable(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)
    address = Column(String(500), nullable=True)
    password = Column(String(100), nullable=False)
    role = Column(String(100), nullable=False, default=RoleUser.User)
    # Relationship to products
