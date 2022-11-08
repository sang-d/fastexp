from typing import List, Union

from fastapi import FastAPI
from pydantic import BaseModel


class CheckList(BaseModel):
    name: str
    description: Union[str, None] = None
    parent_id: Union[int, None] = None
    children: List[int] = []


app = FastAPI()


@app.get("/")
async def root():
    return {"res": "live"}


@app.get("/lists")
async def lists():
    return {"res": []}


@app.get("/list/{list_id}")
async def get_list(list_id: str):
    return {"res": list_id}


@app.post("/list/")
async def create_list(checklist: CheckList):
    return {"res": checklist}


@app.put("/list/{list_id}")
async def update_list(list_id: int, checklist: CheckList):
    return {list_id: checklist}
