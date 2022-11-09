from typing import List, Union

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


class CheckList(BaseModel):
    name: str
    description: Union[str, None] = None
    parent_id: Union[int, None] = None
    children: List[int] = []


app = FastAPI()


my_check_lists = {
    "travel": {
        "documents": ["ticket", "accomodation", "id"],
        "clothes": ["weather", "jacket"],
        "activities": ["shoes", "socks", "gloves", "glasses", "windbreaker"],
        "devices": ["phone", "watch", "charger", "keys"],
        "maintainance": [
            "tooth brusher",
            "razor",
            "foam",
            "anti-mosquito",
            "hankerchief",
        ],
        "stuff": ["gift", "other people items", "give away"],
        "off": ["echo", "hot water", "kitchen"],
        "on": ["autofeeder", "monitoring"],
    }
}


@app.get("/")
async def root():
    return "live"


@app.get("/lists")
async def lists():
    return my_check_lists


@app.get("/list/{list_id}")
async def get_list(list_id: str):
    if list_id not in my_check_lists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="item not found"
        )
    return my_check_lists[list_id]


@app.post("/list/", status_code=status.HTTP_201_CREATED)
async def create_list(alist: CheckList):
    return alist


@app.put("/list/{list_id}")
async def update_list(list_id: str, alist: CheckList):
    return alist
