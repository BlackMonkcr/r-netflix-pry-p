from fastapi import Depends, FastAPI, HTTPException
import uvicorn
from service.profile_service import *
from fastapi.middleware.cors import CORSMiddleware
from typing_extensions import Annotated
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

CORSMiddleware(app, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

# METHODS FOR PROFILES


@app.get("/profiles/")
def read_profiles(id: int):
    profile = get_profile_by_id_services(id)
    return profile

@app.get("/profiles/account/{account_id}")
def read_profiles_by_account_id(account_id: int):
    profiles = get_profiles_by_account_id_services(account_id)
    return profiles

@app.post("/profiles/", response_model=dict)
def create_profile(account_id: int, nombre: str):
    create_profile_service(account_id, nombre)
    return {"message": "Profile created successfully"}

@app.put("/profiles/", response_model=dict)
def update_profile(id: int, nombre: str):
    update_profile_service(id, nombre)
    return {"message": "Profile updated"}

@app.delete("/profiles/", response_model=dict)
def delete_profile(id: int):
    delete_profile_service(id)
    return {"message": "Profile deleted"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, proxy_headers=True, timeout_keep_alive=300)

