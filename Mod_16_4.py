from fastapi import FastAPI, HTTPException, Path
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()


users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users")
async def get_users():
    return users


@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[str, Path(min_length=4, max_length=20, description="Enter username", example="Test")],
        age: Annotated[int, Path(ge=18, le=100, description="Enter age", example=24)]):

    new_id = len(users) + 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example=1)],
        username: Annotated[str, Path(min_length=4, max_length=20, description="Enter username", example="Test")],
        age: Annotated[int, Path(ge=18, le=100, description="Enter age", example=24)]):

    user_to_update = next((user for user in users if user.id == user_id), None)
    if user_to_update is None:
        raise HTTPException(status_code=404, detail=f"The user (id={user_id}) is not found")

    user_to_update.username = username
    user_to_update.age = age
    return user_to_update


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example=1)]):

    user_to_delete = next((user for user in users if user.id == user_id), None)
    if user_to_delete is None:
        raise HTTPException(status_code=404, detail=f"The user (id={user_id}) is not found")

    users.remove(user_to_delete)
    return user_to_delete
