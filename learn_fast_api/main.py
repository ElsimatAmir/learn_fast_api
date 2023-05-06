from fastapi import FastAPI
import uvicorn
from endpoints import user, order
from dataBase.base import engin, Base, db, dataBaseUrl

app = FastAPI(title='TrudyagiRF API')


app.include_router(user.router)
app.include_router(order.router)


@app.on_event("startup")
async def startAt():
    engin = db.create_engine(dataBaseUrl)
    Base.metadata.create_all(bind=engin, checkfirst=True)
    engin.connect()


@app.on_event("shutdown")
async def shutdown():
    engin.dispose()


@app.get('/', tags=['About the API'])
async def root():
    return {"creator": "Elsimat Amir",
            "info": "simple app to order a handymen",
            "country": "will start from Russia Kazan",
            "backEnd": "FastApi + postgreSQL",
            "fronted": "dart + flutter",
            "platform": "mobile(android+Ios)"
            }


if __name__ == "__main__":
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
