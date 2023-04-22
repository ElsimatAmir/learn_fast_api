from pydantic import BaseModel
from datetime import datetime

# TODO: create an orders type list to make a type one of this types
# example: orderTypes = ['worker', ...]


class Order(BaseModel):
    type: str
    description: str
    amount: float
    createAt: datetime
    updatedAt: datetime
    deadlineAt: datetime
