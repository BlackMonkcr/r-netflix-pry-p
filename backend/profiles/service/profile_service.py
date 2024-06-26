from passlib.context import CryptContext
from dotenv import load_dotenv
import os
import psycopg2
from domain.profile_schemas import *

load_dotenv()

host_name = os.getenv("DB_HOST")
port_number = os.getenv("PORT")
user_name = os.getenv("DB_USER")
password_db = os.getenv("DB_PASSWORD")
database_name = os.getenv("DB")

def get_profile_by_id_services(id : int) -> Profile:
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("SELECT id, account_id, nombre FROM perfiles WHERE id=%s", 
                    (str(id)))
    
    result = list(cursor.fetchone())
    result = Profile(result)

    conn.close()
    
    return result

def get_profiles_by_account_id_services(account_id : int) -> list[Profile]:
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("SELECT id, account_id, nombre FROM perfiles WHERE account_id=%s", 
                    (str(account_id)))
    
    result = list(cursor.fetchall())
    result = [Profile(x) for x in result]

    conn.close()
    
    return result

def create_profile_service(account_id: int, nombre: str):
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO perfiles (account_id, nombre) VALUES (%s, %s)", 
                    (str(account_id), nombre))
    conn.commit()
    conn.close()

def update_profile_service(id: int, nombre: str):
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("UPDATE perfiles SET nombre=%s WHERE id=%s", 
                    (nombre, str(id)))
    conn.commit()
    conn.close()

def delete_profile_service(id: int):
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM perfiles WHERE id=%s", (str(id)))
    conn.commit()
    conn.close()
