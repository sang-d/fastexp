from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

items = {}


@app.get("/items/{item_id}")
async def read_items(item_id: str):
    print("debug", item_id, items)
    return items.get(item_id, "")


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "live"


def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    # assert response.json()


def test_get_user_by_name():
    response = client.get("/users/1")
    assert response.status_code == 200
    response = client.get("/users/0")
    assert response.status_code == 404
