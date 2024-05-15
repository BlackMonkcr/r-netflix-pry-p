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

@app.post("/token")
def create_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(form_data.username, form_data.password)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    access_token_expires = timedelta(minutes=float(ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = create_access_token(data={"sub": user.__dict__["email"]}, expires_delta=access_token_expires)
    return Token(access_token=access_token, token_type="bearer")

@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    user = get_current_user(token)
    return user



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, proxy_headers=True, timeout_keep_alive=300)

