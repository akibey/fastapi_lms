from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@app.get(
    "/users", response_model=List[User]
)  # Returns a list of dictionaries and User is dictionary
async def get_users():
    return users


@app.post("/users")
async def create_users(user: User):
    users.append(user)
    return "Success"


@app.get("/users/{id}")
async def get_user(id: int):
    return users[id]
