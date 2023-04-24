from .base import Base
from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Float, Boolean


class OrderDbTable(Base):
    __tablename__ = "orders"
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    ownerId = Column(Integer)
    type = Column(String)
    amount = Column(Float)
    description = Column(String)
    isActive = Column(Boolean, default=True)
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow)
