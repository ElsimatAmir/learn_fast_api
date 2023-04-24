from pydantic import BaseModel
from datetime import datetime

from pyparsing import Optional

# TODO: create an orders type list to make a type one of this types
# example: orderTypes = ['worker', ...]


class Order(BaseModel):
    id: Optional[int]
    ownerId: int
    type: str
    description: str
    amount: float
    createAt: datetime
    updatedAt: datetime
    isActive: bool
