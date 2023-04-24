from fastapi import FastAPI
import uvicorn
from dataBase.base import engin, sessionLocal, Base
from dataBase.order import OrderDbTable
from dataBase.user import UserDbTable
from endpoints.user import router as userRouter
from endpoints.order import router as orderRouter

app = FastAPI()

Base.metadata.create_all(bind=engin, checkfirst=True)

app.include_router(userRouter)
app.include_router(orderRouter)
# Dependency


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

# when the app is start request to exmp: connect to dataBase


@app.on_event("startup")
async def startAt():
    pass
# when the app is start request to exmp: disconnect to dataBase


@app.on_event("shutdown")
async def shutdown():
    pass


@app.get('/')
async def root():
    return {"hello": "world"}


if __name__ == "__main__":
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
