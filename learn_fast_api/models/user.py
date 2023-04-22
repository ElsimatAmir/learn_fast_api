import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr
from order import Order


class User(BaseModel):
    id: Optional[int]
    name: str
    age: bytes
    email: EmailStr
    phoneNumber: int
    hashedPassword: str
    orders: List[Order] = []
    createAt: datetime
    updatedAt: datetime
