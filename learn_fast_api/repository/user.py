from models.user import User, UserInput
from typing import List
from dataBase.base import session
from dataBase.user import UserDbTable
from datetime import datetime


class UserRepository():

    async def getAllUsers() -> List[User]:
        allUsersList = session.query(UserDbTable).all()
        session.commit()
        return allUsersList

    async def createUser(user: UserInput) -> UserDbTable:
        # need to hash the password
        newUser = UserDbTable(**user.dict())

        # session.add(newUser)
        # session.commit()
        return newUser
