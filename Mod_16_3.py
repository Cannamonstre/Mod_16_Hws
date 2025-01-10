from fastapi import FastAPI, HTTPException, Path
from typing import Annotated

app = FastAPI()


users = {"1": "Name: Example, age: 18"}


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[str, Path(min_length=4, max_length=20, description="Enter username", example="Test")],
        age: Annotated[int, Path(ge=18, le=100, description="Enter age", example=24)]):

    max_key = max(int(key) for key in users.keys())
    new_key = str(max_key + 1)
    users[new_key] = f"Name: {username}, age: {age}"
    return f"User (id={new_key}) has been successfully registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example=1)],
        username: Annotated[str, Path(min_length=4, max_length=20, description="Enter username", example="Test")],
        age: Annotated[int, Path(ge=18, le=100, description="Enter age", example=24)]):

    user_id_str = str(user_id)
    if user_id_str not in users:
        raise HTTPException(status_code=404, detail=f"The user (id={user_id_str}) is not found")

    users[user_id_str] = f"Name: {username}, age: {age}"
    return f"The user (id={user_id_str}) has been updated"


@app.delete("/users/{user_id}")
async def delete_user(
        user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example=1)]):

    user_id_str = str(user_id)
    if user_id_str not in users:
        raise HTTPException(status_code=404, detail=f"The user (id={user_id_str}) is not found")

    users.pop(user_id_str)
    return f"The user (id={user_id_str}) has been deleted"
