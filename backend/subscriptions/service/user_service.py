from passlib.context import CryptContext
from dotenv import load_dotenv
import os
import psycopg2
from domain.user_schemas import *

load_dotenv()


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

host_name = os.getenv("DB_HOST")
port_number = os.getenv("PORT")
user_name = os.getenv("DB_USER")
password_db = os.getenv("DB_PASSWORD")
database_name = os.getenv("DB")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hashed_password(password: str) -> str:
    return pwd_context.hash(password)


def get_user_by_id_services(id : int) -> User:
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email FROM accounts WHERE id=%s", 
                    (str(id)))
    
    if cursor.rowcount == 0:
        return None
    
    result = list(cursor.fetchone())
    result = User(result)

    conn.close()
    
    return result

def get_user_by_email_services(email: str) -> UserInDB:
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts WHERE email=%s", 
                    (email,))
    
    if cursor.rowcount == 0:
        return None
    
    result = list(cursor.fetchone())
    result = UserInDB(result)

    conn.close()
    
    return result

def create_user_service(username: str, email: str, password: str):
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO accounts (username, email, password) VALUES (%s, %s, %s)", 
                    (username, email, get_hashed_password(password)))
    conn.commit()
    conn.close()

def update_user_service(id: int, username: str, email: str):
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, username, email FROM accounts WHERE id=%s", 
                    (str(id)))
    
    if cursor.rowcount == 0:
        return None
    
    cursor.execute("UPDATE accounts SET username=%s, email=%s WHERE id=%s", 
                    (username, email, id))
    
    conn.commit()
    conn.close()

def delete_user_service(id: int):
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()

    cursor.execute("SELECT id, username, email FROM accounts WHERE id=%s", 
                    (str(id)))
    
    if cursor.rowcount == 0:
        return None
    
    cursor.execute("DELETE FROM accounts WHERE id=%s", (id,))
    conn.commit()
    conn.close()
