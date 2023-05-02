from models.user import User, UserInput
from typing import List
from dataBase.base import session
from dataBase.user import UserDbTable


class UserRepository():

    async def getAllUsers() -> List[User]:
        allUsersList = session.query(UserDbTable).all()
        session.commit()
        return allUsersList

    async def createUser(user: UserInput) -> User:
        newUser = User(
            name=user.name,
            age=user.age,
            email=user.email,
            phoneNumber=user.phoneNumber,
            hashedPassword=user.password,
        )

        print(newUser)  # need to be deleted after a debug
        # session.add(newUser)
        # session.commit()
        return user
