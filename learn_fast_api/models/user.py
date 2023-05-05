import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: Optional[int]
    name: str
    age: int
    email: EmailStr
    phoneNumber: int
    hashedPassword: str
    orders: int
    successOrder: int
    cancelOrder: int
    createdAt: datetime.datetime
    updatedAt: datetime.datetime

    class Config:
        orm_mode = True

    # def __init__(self, id, name, age, email, password, phoneNumber, orders, successOrder, cancelOrder, createAt, updatedAt):
    #     super().__init__
    #     self.id = id
    #     self.name = name
    #     self.age = age
    #     self.email = email
    #     self.hashedPassword = password
    #     self.phoneNumber = phoneNumber
    #     self.orders = orders
    #     self.successOrder = successOrder
    #     self.cancelOrder = cancelOrder
    #     self.createdAt = createAt
    #     self.updatedAt = updatedAt


class UserInput(BaseModel):
    name: str
    age: int
    email: EmailStr
    phoneNumber: int
    hashedPassword: str

    class Config:
        orm_mode = True
