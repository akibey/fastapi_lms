from fastapi import FastAPI

app = FastAPI()

users = []


@app.get("/users")
async def get_users():
    return users


@app.post("/users")
async def create_users(user):
    users.append(user)
    return "Success"
