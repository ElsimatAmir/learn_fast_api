from fastapi import APIRouter
from repository.user import UserRepository
from models.user import User, UserInput
from typing import List

router = APIRouter(prefix='/api/user', tags=['UserApi'])


@router.get("/getAllUsers", response_model=List[User])
async def getAllUsers() -> List[User]:
    allUsersList = await UserRepository.getAllUsers()
    return allUsersList


@router.post("/getUserById", response_model=User)
async def GetUserById(userId: int) -> User:
    pass


@router.post("/getUserByEmail", response_model=User)
async def GetUserById(userEmail: str) -> User:
    pass


@router.post("/createUser")  # , response_model=User
async def createUser(userInputData: UserInput):
    newUser = await UserRepository.createUser(userInputData)
    return newUser
