from sqlalchemy import create_engine
from core.secretData import secretData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

dataBaseUrl = secretData["LEARN_FASTAPI_DB_URL"]

engin = create_engine(dataBaseUrl)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engin)

Base = declarative_base()
