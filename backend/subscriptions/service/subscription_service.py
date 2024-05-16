from passlib.context import CryptContext
from dotenv import load_dotenv
import os
import psycopg2
from domain.subscription_schemas import *
from datetime import date, timedelta

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

host_name = os.getenv("DB_HOST")
port_number = os.getenv("PORT")
user_name = os.getenv("DB_USER")
password_db = os.getenv("DB_PASSWORD")
database_name = os.getenv("DB")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def getAllSubscriptions() -> list[Subscription]:
    conn = psycopg2.connect(
      host=host_name,
      port=port_number,
      user=user_name,
      password=password_db,
      database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subscriptions")
    
    result = list(cursor.fetchall())
    result = [Subscription(x) for x in result]

    conn.close()
    
    return result


def getSubscriptionById(id : int) -> Subscription:
    conn = psycopg2.connect(
      host=host_name,
      port=port_number,
      user=user_name,
      password=password_db,
      database=database_name
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subscriptions WHERE id=%s",
                    (str(id)))
    
    result = list(cursor.fetchone())
    result = Subscription(result)

    conn.close()

    return result

def getSubscriptionsByAccountId(account_id : int) -> Subscription:
    conn = psycopg2.connect(
      host=host_name,
      port=port_number,
      user=user_name,
      password=password_db,
      database=database_name
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subscriptions WHERE account_id=%s",
                    (str(account_id)))
    
    result = list(cursor.fetchone())
    result = Subscription(result)

    conn.close()

    return result

def createSubscription(account_id: int, plan: str, start_date: str, status: str):
    # end_date is calculated (start_date + 30 days)
    end_date = date.fromisoformat(start_date) + timedelta(days=30)
    conn = psycopg2.connect(
      host=host_name,
      port=port_number,
      user=user_name,
      password=password_db,
      database=database_name
    )

    cursor = conn.cursor()
    cursor.execute("INSERT INTO subscriptions (account_id, plan, start_date, end_date, status) VALUES (%s, %s, %s, %s, %s)",
                    (str(account_id), plan, start_date, str(end_date), status))
    
    conn.commit()
    conn.close()

def deleteSubscription(id: int):
    conn = psycopg2.connect(
      host=host_name,
      port=port_number,
      user=user_name,
      password=password_db,
      database=database_name
    )

    cursor = conn.cursor()
    cursor.execute("DELETE FROM subscriptions WHERE id=%s",
                    (str(id)))
    
    conn.commit()
    conn.close()