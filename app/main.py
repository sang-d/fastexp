import time

from fastapi import FastAPI, Request

from app.db import models
from app.db.database import engine
from app.routers import lists, users

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(lists.router)


@app.get("/")
async def root():
    return "live"


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
