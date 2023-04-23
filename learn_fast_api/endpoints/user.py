from fastapi import APIRouter

router = APIRouter()


@router.get("/api/users")
def getAllUsers():
    pass
