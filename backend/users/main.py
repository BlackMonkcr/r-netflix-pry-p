from fastapi import Depends, FastAPI, HTTPException
import uvicorn
from service.user_service import *
from service.profile_service import *
from service.token_service import *
from domain.token import Token
from fastapi.middleware.cors import CORSMiddleware
from typing_extensions import Annotated
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

CORSMiddleware(app, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

# METHODS FOR USERS


@app.get("/users/")
def read_users(id: int):
    user = get_user_by_id_services(id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users/", response_model=dict)
def create_user(username: str, email: str, password: str):
    create_user_service(username, email, password)
    return {"message": "User created successfully"}

@app.put("/users/", response_model=dict)
def update_user(id: int, username: str, email: str):
    if update_user_service(id, username, email) is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated"}

@app.delete("/users/", response_model=dict)
def delete_user(id: int):
    if delete_user_service(id) is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, proxy_headers=True, timeout_keep_alive=300)

