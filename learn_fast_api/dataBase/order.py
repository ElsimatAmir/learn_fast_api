from .base import metaData
from datetime import datetime
from sqlalchemy import Column, Table, DateTime, Integer, String, Float, Boolean
import sqlalchemy as sql

orderDbTable = Table(
    'orders',
    metaData,
    Column('id', Integer,
           autoincrement=True, primary_key=True, unique=True),
    Column('type', String),
    Column('amount', Float),
    Column('discreption', String),
    Column('isActive', Boolean),
    Column('createdAt', DateTime,
           default=datetime.utcnow),
    Column('updatedAt', DateTime,
           default=datetime.utcnow),
)
