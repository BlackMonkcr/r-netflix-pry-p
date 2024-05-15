from fastapi import Depends, FastAPI, HTTPException
import uvicorn
from service.subscription_service import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

CORSMiddleware(app, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


@app.get("/subscriptions")
async def get_subscriptions():
    return getAllSubscriptions()


@app.get("/subscriptions/{id}")
async def get_subscription_by_id(id: int):
    return getSubscriptionById(id)


@app.get("/subscriptions/account/{account_id}")
async def get_subscriptions_by_account_id(account_id: int):
    return getSubscriptionsByAccountId(account_id)


@app.post("/subscriptions")
async def create_subscription(account_id: int, plan: str, start_date: str, end_date: str, status: str):
    return createSubscription(SubscriptionCreate([account_id, plan, start_date, end_date, status]))


@app.delete("/subscriptions/{id}")
async def delete_subscription(id: int):
    return deleteSubscription(id)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, proxy_headers=True, timeout_keep_alive=300)

