from fastapi import Depends, FastAPI, HTTPException
import uvicorn
from service.content_service import *
from fastapi.middleware.cors import CORSMiddleware
from typing_extensions import Annotated
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

# Configura los orígenes permitidos
origins = [
    "*",
    # Otros orígenes que quieras permitir
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE")

# METHODS FOR CONTENT

@app.get("/content/")
def read_all_content():
    content = getAllContent_service()
    return {"results": content}

@app.get("/content/{id}")
def read_content_by_id(id: int):
    content = get_content_by_id_service(id)
    if content is None:
        raise HTTPException(status_code=404, detail="Content not found")
    return content

@app.get("/content/type/{type}")
def read_content_by_type(type: str):
    content = get_content_by_type_service(type)
    if content is None:
        raise HTTPException(status_code=404, detail="Content not found")
    return {"results": content}

@app.post("/content/", response_model=dict)
def create_content(title: str, description: str, release_date: str, type: str, url_content: str, url_cover: str):
    create_content_service(title, description, release_date, type, url_content, url_cover)
    return {"message": "Content created successfully"}

@app.delete("/content/{id}", response_model=dict)
def delete_content(id: int):
    if (delete_content_service(id) is None):
        raise HTTPException(status_code=404, detail="Content not found")
    return {"message": "Content deleted"}

@app.put("/content/", response_model=dict)
def patchTitleContent(id: int, title: str):
    if (patch_title_content_service(id, title) is None):
        raise HTTPException(status_code=404, detail="Content not found")
    return {"message": "Title updated"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, proxy_headers=True, timeout_keep_alive=300)
