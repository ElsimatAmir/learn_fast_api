from fastapi import APIRouter
from repository.user import UserRepository
from models.user import User, UserInput, UserOutput
from typing import List

router = APIRouter(prefix='/api/user', tags=['UserApi'])


@router.get("/getAllUsers", response_model=List[UserOutput])
async def getAllUsers(skip: int = 0, limit: int = 10) -> List[UserOutput]:
    allUsersList = await UserRepository.getAllUsers(limit, skip)
    return allUsersList


@router.post("/getUserById", response_model=UserOutput)
async def GetUserById(userId: int) -> UserOutput:
    pass


@router.post("/getUserByEmail", response_model=UserOutput)
async def GetUserById(userEmail: str) -> UserOutput:
    pass


@router.post("/createUser", response_model=UserOutput)
async def createUser(userInputData: UserInput) -> UserOutput:
    newUser = await UserRepository.createUser(userInputData)
    return newUser
