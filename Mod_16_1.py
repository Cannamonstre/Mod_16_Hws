from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main_page():
    return "Main Page"


@app.get("/user/admin")
async def admin_page():
    return "You're logged in as an admin"


@app.get("/user/{user_id}")
async def user_info(user_id: int):
    return f"You're logged in as user # {user_id}"


@app.get("/user")
async def user_extended_info(username: str, age: int):
    return f"User info - username: {username}, age: {age}"
