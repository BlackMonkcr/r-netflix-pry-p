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

def getAllContent_service() -> list[Content]:
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("SELECT title, description, release_date, type, url_content, url_cover, id FROM content")
    
    result = list(cursor.fetchall())
    result = [Content(x) for x in result]

    conn.close()
    
    return result

def get_content_by_id_service(id: int) -> Content:
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("SELECT title, description, release_date, type, url_content, url_cover, id FROM content WHERE id=%s", 
                    (str(id),))
    
    result = cursor.fetchone()
    result = Content(result)

    conn.close()
    
    return result


def get_content_by_type_service(type : str) -> Content:
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("SELECT title, description, release_date, type, url_content, url_cover, id FROM content WHERE type=%s", 
                    (type,))
    
    if cursor.rowcount == 0:
        return None
    
    result = cursor.fetchone()
    result = Content(result)

    conn.close()
    
    return result

def create_content_service(title: str, description: str, release_date, type: str, url_content: str, url_cover: str):
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO content (title, description, release_date, type, url_content, url_cover) VALUES (%s, %s, %s, %s, %s, %s)", 
                    (title, description, release_date, type, url_content, url_cover))
    conn.commit()
    conn.close()

def patch_title_content_service(id: int, title: str):
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM content WHERE id=%s", 
                    (str(id),))
    if cursor.rowcount == 0:
        return None
    
    cursor.execute("UPDATE content SET title=%s WHERE id=%s", 
                    (title, str(id)))

    conn.commit()
    conn.close()

def patch_description_service(id: int, description: str):
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("SELECT title, description, release_date, type, url_content, url_cover, id FROM content WHERE id=%s", 
                    (str(id),))
    if cursor.rowcount == 0:
        conn.close()
        return None
    cursor.execute("UPDATE content SET description=%s WHERE id=%s", 
                    (description, str(id)))
    conn.commit()
    conn.close()

def patch_urlCover_service(id: int, url_cover: str):
    conn = psycopg2.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )
    cursor = conn.cursor()
    cursor.execute("SELECT title, description, release_date, type, url_content, url_cover, id FROM content WHERE id=%s", 
                (str(id),))
    if cursor.rowcount == 0:
        conn.close()
        return None
    cursor.execute("UPDATE content SET url_cover=%s WHERE id=%s", 
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
    cursor.execute("SELECT title, description, release_date, type, url_content, url_cover, id FROM content WHERE id=%s", 
                    (str(id),))
    if cursor.rowcount == 0:
        conn.close()
        return None
    cursor.execute("DELETE FROM content WHERE id=%s", 
                    (str(id)))
    conn.commit()
    conn.close()