from fastapi import FastAPI

from app.db import models
from app.db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# DependencyO
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
