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
        # need to hash the password
        newUser = UserDbTable(**user.dict())
        session.add(newUser)
        session.commit()

        userModel = User(id=newUser.id, name=newUser.name, age=newUser.age, hashedPassword=newUser.hashedPassword, phoneNumber=newUser.phoneNumber, email=newUser.email,
                         createdAt=newUser.createdAt, updatedAt=newUser.updatedAt, orders=newUser.orders, successOrder=newUser.successOrders, cancelOrder=newUser.cancelOrders)

        print(userModel)

        return userModel
