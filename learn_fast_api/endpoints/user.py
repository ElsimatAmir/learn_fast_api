from fastapi import APIRouter
from repository.user import UserRepository

router = APIRouter()


@router.get("/api/users")
def getAllUsers():
    pass
