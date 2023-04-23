from sqlalchemy import Column, Table, DateTime, Integer, String, ARRAY
from .base import Base
from datetime import datetime


class UserDbtable(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String, unique=True)
    phoneNumber = Column(Integer)
    hashedBassword = Column(String)
    orders = Column(Integer)
    successedOrders = Column(Integer)
    canceldOrders = Column(Integer)
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow)
