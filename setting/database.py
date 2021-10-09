import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
import os
from dotenv import load_dotenv

load_dotenv()


db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_name = os.getenv("DB_NAME")
db_host = os.getenv("DB_HOST")


def initialize_local_db():
    url = URL(
        drivername="mysql+pymysql",
        username=db_user,
        host=db_host,
        password=db_pass,
        database=db_name,
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
