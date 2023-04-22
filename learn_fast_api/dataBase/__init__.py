from .base import metaData, engin

metaData.create_all(bind=engin)
print(metaData.info)
