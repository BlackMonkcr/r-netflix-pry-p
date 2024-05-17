from passlib.context import CryptContext
from dotenv import load_dotenv
import os
import psycopg2
from domain.interaction_schemas import *
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

def getAllInteractions() -> list[Interaction]:
    conn = psycopg2.connect(
      host=host_name,
      port=port_number,
      user=user_name,
      password=password_db,
      database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM interacciones")
    
    result = list(cursor.fetchall())
    result = [Interaction(x) for x in result]

    conn.close()
    
    return result


def getInteractionsByAccountId(account_id : int) -> Interaction:
    conn = psycopg2.connect(
      host=host_name,
      port=port_number,
      user=user_name,
      password=password_db,
      database=database_name
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM interacciones WHERE account_id=%s",
                    (str(account_id)))
    
    result = list(cursor.fetchall())
    result = [Interaction(x) for x in result]

    conn.close()

    return result

def getInteractionsByContentId(content_id : int) -> Interaction:
    conn = psycopg2.connect(
      host=host_name,
      port=port_number,
      user=user_name,
      password=password_db,
      database=database_name
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM interacciones WHERE content_id=%s",
                    (str(content_id)))
    
    result = list(cursor.fetchall())
    result = [Interaction(x) for x in result]

    conn.close()

    return result

def createInteraction(account_id: int, content_id: int, interaction_type: str):
    # end_date is calculated (start_date + 30 days)
    conn = psycopg2.connect(
      host=host_name,
      port=port_number,
      user=user_name,
      password=password_db,
      database=database_name
    )

    cursor = conn.cursor()
    cursor.execute("INSERT INTO interacciones (account_id, content_id, interaction_type) VALUES (%s, %s, %s)",
                    (str(account_id), str(content_id), interaction_type))
    
    conn.commit()
    conn.close()

def deleteInteraction(id: int):
    conn = psycopg2.connect(
      host=host_name,
      port=port_number,
      user=user_name,
      password=password_db,
      database=database_name
    )

    cursor = conn.cursor()
    cursor.execute("DELETE FROM interacciones WHERE id=%s",
                    (str(id)))
    
    conn.commit()
    conn.close()