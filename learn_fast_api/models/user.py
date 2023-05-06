import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: Optional[int]
    name: str
    age: int
    email: EmailStr
    phoneNumber: str
    hashedPassword: str
    orders: int
    successOrder: int
    cancelOrder: int
    createdAt: datetime.datetime
    updatedAt: datetime.datetime

    class Config:
        orm_mode = True


class UserInput(BaseModel):
    name: str
    age: int
    email: EmailStr
    phoneNumber: str
    hashedPassword: str

    class Config:
        orm_mode = True
