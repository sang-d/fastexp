import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

username = os.environ.get("MYSQL_USERNAME")
password = os.environ.get("MYSQL_PWD")
host = os.environ.get("MYSQL_HOST")
port = os.environ.get("MYSQL_PORT")
dbname = "fastexp"

SQLALCHEMY_DATABASE_URL = f"mysql://{username}:{password}@{host}:{port}/{dbname}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
