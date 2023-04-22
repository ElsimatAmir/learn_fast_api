from fastapi import FastAPI

app = FastAPI()

# when the app is start request to exmp: connect to dataBase


@app.on_event("startup")
async def startAt():
    pass

# when the app is start request to exmp: connect to dataBase


@app.on_event("shutdown")
async def shutdown():
    pass


@app.get('/')
async def root():
    return {"hello": "world"}
