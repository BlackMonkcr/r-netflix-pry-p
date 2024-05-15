from datetime import datetime, timedelta, timezone
import requests
from typing import Union
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from dotenv import load_dotenv
import os
from domain.user_schemas import User, UserInDB
from domain.token import TokenData

load_dotenv()

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)

def fetch_data(route: str, headers: dict = {}, params: dict = {}, method: str = "GET"):
    # Realiza una solicitud GET a una URL
    route = "http://localhost:8003/" + route
    if method == "GET":
        response = requests.get(route, headers=headers, params=params)
    # Realiza una solicitud POST a una URL
    elif method == "POST":
        response = requests.post(route, headers=headers, params=params)
    # Realiza una solicitud PUT a una URL
    elif method == "PUT":
        response = requests.put(route, headers=headers, params=params)
    # Realiza una solicitud DELETE a una URL
    elif method == "DELETE":
        response = requests.delete(route, headers=headers, params=params)
    # Realiza una solicitud PATCH a una URL
    elif method == "PATCH":
        response = requests.patch(route, headers=headers, params=params)

    # Verifica si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Devuelve los datos obtenidos de la solicitud
        return response.json()
    else:
        # Si la solicitud no fue exitosa, devuelve un mensaje de error
        return {"error": "No se pudo obtener los datos"}


def authenticate_user(email: str, password: str):
    user : UserInDB = fetch_data(f"users/email/?email={email.replace('@', '%40')}")

    print(user["password"])
    
    if not user:
        return False
    if not verify_password(password, user["password"]):
        return False
    return User([user["id"], user["username"], user["email"]])


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user : UserInDB = fetch_data(f"users/email/?email={email}")
    if user is None:
        raise credentials_exception
    return user