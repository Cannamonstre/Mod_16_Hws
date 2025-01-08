from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()


@app.get("/")
async def main_page():
    return "Main Page"


@app.get("/user/admin")
async def admin_page():
    return "You're logged in as an admin"


@app.get("/user/{user_id}")
async def user_info(
        user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example=1)]):
    return f"You're logged in as user # {user_id}"


@app.get("/user/{username}/{age}")
async def user_extended_info(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="Tester")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]):
    return f"User info - username: {username}, age: {age}"
