from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config_data import config

from sqlalchemy.orm import DeclarativeBase

from config import settings


engine = create_engine(
	config.DATABASE_URL, connect_args={"check_same_thread": False}
)
engine.connect()

SessionLocal = sessionmaker(
	autocommit=False, autoflush=False, bind=engine
)


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(naming_convention=settings.database.naming_convention)

