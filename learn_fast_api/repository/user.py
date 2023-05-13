from models.user import UserLogin, UserInput, UserOutput
from typing import List
from dataBase.base import session
from dataBase.user import UserDbTable
from auth.security import hash, verify
from auth.access_token import signToken


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

    async def loginUser(userLogin: UserLogin):
        currentUser = session.query(UserDbTable).filter(
            UserDbTable.email == userLogin.login or UserDbTable.phoneNumber == userLogin.login).first()
        if currentUser == None:
            return {
                'Error': 'invalid Email or phone number'
            }
        else:
            isPasswordCorrect = verify(
                password=userLogin.hashedPassword, hashedPassword=currentUser.hashedPassword)
            if isPasswordCorrect:
                return signToken(currentUser.id)
            else:
                return {
                    "Error": "invalid password"
                }
