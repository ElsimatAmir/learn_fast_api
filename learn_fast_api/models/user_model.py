
from pydantic import BaseModel


class User(BaseModel):
    name: str | None
    age: int | None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setName(name: str):
        name = name
