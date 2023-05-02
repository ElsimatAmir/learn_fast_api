import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: Optional[int]
    name: str
    age: bytes
    email: EmailStr
    phoneNumber: int
    hashedPassword: str
    orders: int
    successOrder: int
    cancelOrder: int
    createAt: datetime.datetime
    updatedAt: datetime.datetime

    def __init__(self, name, age, email, phoneNumber, hashedPassword):
        self.name = name
        self.age = age
        self.email = email
        self.phoneNumber = phoneNumber
        self.hashedPassword = hashedPassword
        self.orders, self.cancelOrder, self.successOrder = 0
        self.createAt, self.updatedAt = datetime.datetime.utcnow()


class UserInput(BaseModel):
    name: str
    age: int
    email: EmailStr
    phoneNumber: int
    password: str
