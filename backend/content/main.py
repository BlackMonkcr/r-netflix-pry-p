from fastapi import Depends, FastAPI, HTTPException
import uvicorn
from service.content_service import *
from fastapi.middleware.cors import CORSMiddleware
from typing_extensions import Annotated
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

CORSMiddleware(app, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE")

# METHODS FOR CONTENT

@app.get("/content/")
def read_all_content():
    content = getAllContent()
    return content

@app.get("/content/type/{type}")
def read_content_by_type(type: str):
    content = get_content_by_type(type)
    return content

@app.post("/content/", response_model=dict)
def create_content(title: str, description: str, type: str, url_content: str, url_cover: str):
    create_content(title, description, type, url_content, url_cover)
    return {"message": "Content created successfully"}

@app.delete("/content/{id}", response_model=dict)
def delete_content(id: int):
    delete_content(id)
    return {"message": "Content deleted"}

@app.put("/content/", response_model=dict)
def patchTitleContent(id: int, title: str):
    patch_title_content(id, title)
    return {"message": "Title updated"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, proxy_headers=True, timeout_keep_alive=300)