from passlib.context import CryptContext
from dotenv import load_dotenv
import os
import psycopg2
from domain.content_schemas import *

load_dotenv()

host_name = os.getenv("DB_HOST")
port_number = os.getenv("PORT")
user_name = os.getenv("DB_USER")
password_db = os.getenv("DB_PASSWORD")
database_name = os.getenv("DB")

def getAllContent() -> list[Content]:
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contenido")
    
    result = list(cursor.fetchall())
    result = [Content(x) for x in result]

    conn.close()
    
    return result

def get_content_by_id(id: int) -> Content:
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contenido WHERE id=%s", 
                    (str(id),))
    
    result = cursor.fetchone()
    result = Content(result)

    conn.close()
    
    return result


def get_content_by_type(type : str) -> Content:
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contenido WHERE type=%s", 
                    (type,))
    
    result = cursor.fetchone()
    result = Content(result)

    conn.close()
    
    return result

def create_content(account_id: int, title: str, description: str, type: str, url_content: str, url_cover: str):
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contenido (account_id, title, description, type, url_content, url_cover) VALUES (%s, %s, %s, %s, %s, %s)", 
                    (str(account_id), title, description, type, url_content, url_cover))
    conn.commit()
    conn.close()

def patch_title_content(id: int, title: str):
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("UPDATE contenido SET title=%s WHERE id=%s", 
                    (title, str(id)))
    conn.commit()
    conn.close()

def patch_description(id: int, description: str):
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("UPDATE contenido SET description=%s WHERE id=%s", 
                    (description, str(id)))
    conn.commit()
    conn.close()

def patch_urlCover(id: int, url_cover: str):
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("UPDATE contenido SET url_cover=%s WHERE id=%s", 
                    (url_cover, str(id)))
    conn.commit()
    conn.close()

def delete_content_service(id: int):
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contenido WHERE id=%s", 
                    (str(id)))
    conn.commit()
    conn.close()