import time
from typing import List, Union

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class CheckList(BaseModel):
    name: str
    description: Union[str, None] = None
    parent_id: Union[int, None] = None
    children: List[int] = []


app = FastAPI()

# app.add_middleware(HTTPSRedirectMiddleware)
origins = ["http://localhost", "http://localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


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
    },
    "coffee-workspace": {
        "devices": ["laptop", "phone", "ear-phone", "watch"],
        "clothes": ["casual", "formal"],
        "stationeries": ["pen", "note"],
        "utilities": [
            "tissue",
            "wet-tissue",
            "eye-drop",
            "mosquito repellent",
            "cleaning gel",
        ],
        "others": ["book"],
    },
    "decision-making": {
        "logical-reasoning": {
            "situation": "logical, reasoning, analysis, scientific",
            "strategies": [
                "getting more info/data",
                "fat-tail effect awareness",
                "flexible options",
            ],
        },
        "instinct": {
            "situation": "quick, no data, type two decision",
            "strategies": [
                "push back",
                "delay",
                "run",
                "redirect",
                "engaging",
                "clarifying",
            ],
        },
        "consulting": {
            "situation": "complicated, complex, technical, unfarmiliar domain",
            "strategies": [
                "seek expert opinion",
                "search online",
                "forum",
                "friend, family",
            ],
        },
        "future-look-back": {
            "situation": "long term effect, type one, hard to revert, moral, ethical, visionary, discipline",
            "strategies": [
                "vocal declaration",
                "public validation",
                "lock committment",
            ],
        },
        "put-other-in-your-shoes": {
            "situation": "need objective view, realistic self-assessment, self-evaluation, moral, ethical",
            "strategies": [
                "decision would you advise your children/love/friend to make",
                "decision your enemy would make",
                "decision wise people would make",
            ],
        },
    },
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
