import sqlalchemy as db
from core.secretData import secretData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

dataBaseUrl = secretData["LEARN_FASTAPI_DB_URL"]

Base = declarative_base()

engin = db.create_engine(dataBaseUrl)

Base.metadata.create_all(bind=engin, checkfirst=True)

Session = sessionmaker(bind=engin)

session = Session()
