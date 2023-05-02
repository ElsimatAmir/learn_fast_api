from sqlalchemy import Column, DateTime, Integer, String
from .base import Base
from datetime import datetime


class UserDbTable(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String, unique=True)
    phoneNumber = Column(Integer)
    hashedPassword = Column(String)
    orders = Column(Integer, default=0)
    successOrders = Column(Integer, default=0)
    cancelOrders = Column(Integer, default=0)
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow)
