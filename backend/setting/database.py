import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
import os
from dotenv import load_dotenv

load_dotenv()


user_name = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
host =os.getenv("DB_HOST")
database_name =  os.getenv("DB_NAME")



def initialize_local_db():
    url = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    user_name,
    password,
    host,
    database_name,
    )

    return sqlalchemy.create_engine(url)


engine = initialize_local_db()

Session = sessionmaker(bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = Session()
        yield db
    finally:
        db.close()


def get_db_return():
    try:
        db = Session()
        return db
    finally:
        db.close()


def get_db_sync():
    db = Session()
    return db
