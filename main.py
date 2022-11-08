from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome"}


@app.get("/lists")
async def lists():
    return {"message": "return list of lists"}


@app.get("/list/{list_id}")
async def get_list(list_id: str):
    return {"message": list_id}


@app.post("/list/")
async def post_list():
    return {"message"}
