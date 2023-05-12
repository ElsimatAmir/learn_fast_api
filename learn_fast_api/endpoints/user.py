from fastapi import APIRouter
from repository.user import UserRepository
from models.user import User, UserInput, UserOutput
from typing import List

router = APIRouter(prefix='/api/user', tags=['UserApi'])


@router.get("/getAllUsers", response_model=List[UserOutput])
async def getAllUsers(skip: int = 0, limit: int = 10) -> List[UserOutput]:
    allUsersList = await UserRepository.getAllUsers(limit, skip)
    return allUsersList


@router.post("/getUserById/userID={userId}", response_model=UserOutput)
async def GetUserById(userId: int) -> UserOutput:
    user = await UserRepository.getUserById(userId)
    return user


@router.post("/getUserByPhoneNumber/phoneNumber={userPhoneNumber}", response_model=UserOutput)
async def GetUserById(userPhoneNumber: str) -> UserOutput:
    user = await UserRepository.getUserByPhoneNumber(userPhoneNumber)
    return user


@router.post("/getUserByEmail/userEmail={userEmail}", response_model=UserOutput)
async def GetUserById(userEmail: str) -> UserOutput:
    user = await UserRepository.getUserByEmail(userEmail)
    return user


@router.post("/createUser", response_model=UserOutput)
async def createUser(userInputData: UserInput) -> UserOutput:
    newUser = await UserRepository.createUser(userInputData)
    return newUser
