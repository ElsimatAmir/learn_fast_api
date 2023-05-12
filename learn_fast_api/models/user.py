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
    successOrders: int
    cancelOrders: int
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


class UserOutput(BaseModel):
    id: Optional[int]
    name: str
    age: int
    email: EmailStr
    phoneNumber: str
    orders: int
    successOrders: int
    cancelOrders: int
    createdAt: datetime.datetime
    updatedAt: datetime.datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    login: str
    hashedPassword: str

    class Config:
        orm_mode = True
