from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from .base import Base
from datetime import datetime


class UserDbTable(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String(115))
    age = Column(Integer)
    email = Column(String(115), unique=True)
    phoneNumber = Column(String(115), unique=True)
    hashedPassword = Column(String(115))
    orders = Column(Integer, default=0)
    successOrders = Column(Integer, default=0)
    cancelOrders = Column(Integer, default=0)
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow)
