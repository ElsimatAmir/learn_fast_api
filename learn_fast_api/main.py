from fastapi import FastAPI
from dataBase.base import db
import uvicorn

app = FastAPI()

# when the app is start request to exmp: connect to dataBase


@app.on_event("startup")
async def startAt():
    try:
        await db.connect()

    except:
        print("cannot connect to the data base")

# when the app is start request to exmp: disconnect to dataBase


@app.on_event("shutdown")
async def shutdown():
    return await db.disconnect()


@app.get('/')
async def root():
    return {"hello": "world"}


if __name__ == "__main__":
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
