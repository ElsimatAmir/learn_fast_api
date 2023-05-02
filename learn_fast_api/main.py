from fastapi import FastAPI
import uvicorn
from dataBase.base import engin, Base
from endpoints import user, order
from dataBase.base import engin

app = FastAPI(title='TrudyagiRF API')


app.include_router(user.router)
app.include_router(order.router)


@app.on_event("startup")
async def startAt():
    engin.connect()


@app.on_event("shutdown")
async def shutdown():
    engin.dispose()


@app.get('/')
async def root():
    return {"hello": "world"}


if __name__ == "__main__":
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
