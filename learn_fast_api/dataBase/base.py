from databases import Database
from sqlalchemy import create_engine, MetaData
from core.secretData import secretData

dataBaseUrl = secretData["LEARN_FASTAPI_DB_URL"]

db = Database(dataBaseUrl)
metaData = MetaData()
engin = create_engine(
    dataBaseUrl
)


async def initDataBase():
    await metaData.create_all(engin)
