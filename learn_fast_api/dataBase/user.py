from sqlalchemy import Column, Table, DateTime, Integer, String, ARRAY
from .base import metaData
from datetime import datetime

userDbTable = Table(
    'users',
    metaData,
    Column('id', Integer,
           autoincrement=True, primary_key=True, unique=True),
    Column('name', String),
    Column('age', Integer),
    Column('email', String,
           unique=True, primary_key=True),
    Column('phoneNumber', Integer),
    Column('hashedBassword', String),
    Column('orders', ARRAY(str)),
    Column('createdAt', DateTime,
           default=datetime.utcnow),
    Column('updatedAt', DateTime,
           default=datetime.utcnow),

)
