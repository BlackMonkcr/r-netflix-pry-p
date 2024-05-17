from fastapi import Depends, FastAPI, HTTPException
import uvicorn
from service.interaction_service import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

CORSMiddleware(app, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


@app.get("/interactions")
async def get_interactions():
    return getAllInteractions()


@app.get("/interactions/account/{id}")
async def get_interactions_by_account_id(id: int):
    return getInteractionsByAccountId(id)


@app.get("/interactions/content/{id}")
async def get_interactions_by_content_id(id: int):
    return getInteractionsByContentId(id)


@app.post("/interactions")
async def create_interactions(account_id: int, content_id: int, interaction_type: str):
    return createInteraction(account_id, content_id, interaction_type)

@app.delete("/interactions/{id}")
async def delete_interactions(id: int):
    if (deleteInteraction(id) is None):
        raise HTTPException(status_code=404, detail="Subscription not found")
    return {"message": "Subscription deleted"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, proxy_headers=True, timeout_keep_alive=300)

