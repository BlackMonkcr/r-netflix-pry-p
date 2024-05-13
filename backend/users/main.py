from fastapi import Depends, FastAPI, HTTPException
import uvicorn
from service.user_service import *
from domain.user_schemas import User
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

CORSMiddleware(app, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# Dependency

@app.get("/users/")
def read_users(id: int):
    user = get_user_by_id_services(id)
    return user

@app.post("/users/")
def create_user(username: str, email: str, password: str):
    create_user_service(username, email, password)
    return {"message": "User created successfully"}

@app.put("/users/")
def update_user(id: int, username: str, email: str):
    update_user_service(id, username, email)
    return {"message": "User updated"}

@app.delete("/users/")
def delete_user(id: int):
    delete_user_service(id)
    return {"message": "User deleted"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, proxy_headers=True, timeout_keep_alive=300)
