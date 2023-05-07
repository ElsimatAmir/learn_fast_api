from models.user import User, UserInput, UserOutput
from typing import List
from dataBase.base import session
from dataBase.user import UserDbTable
from auth.security import hash


class UserRepository():

    async def getAllUsers(skip: int, limit: int) -> List[UserOutput]:
        # TODO ADD after fix -> .offset(skip).limit(limit) getting empty list
        allUsersList = session.query(UserDbTable).all()
        print(allUsersList)
        session.commit()
        return allUsersList

    async def getUserById(userId: str) -> UserOutput:
        user = session.query(UserDbTable).filter(
            UserDbTable.id == userId).first()
        return user

    async def getUserByEmail(userEmail: str) -> UserOutput:
        user = session.query(UserDbTable).filter(
            UserDbTable.email == userEmail).first()
        return user

    async def getUserByPhoneNumber(userPhoneNumber: str) -> UserOutput:
        user = session.query(UserDbTable).filter(
            UserDbTable.phoneNumber == userPhoneNumber).first()
        return user

    async def createUser(user: UserInput) -> UserOutput:
        user.hashedPassword = hash(user.hashedPassword)
        newUser = UserDbTable(**user.dict())
        session.add(newUser)
        session.commit()
        return newUser
