from fastapi import FastAPI
import uvicorn

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


if __name__ == "__main__":
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
