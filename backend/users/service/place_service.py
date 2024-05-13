from sqlalchemy.orm import Session

from domain.models import Place as PlaceModel
from domain.dtos.place_schemas import PlaceCreate, Place, listPlace
from fastapi import HTTPException, status
import re


def transform_place_to_place_schema(place: PlaceModel) -> Place:
    return Place(
        id=place.id,
        name=place.name,
        city=place.city,
        location_url=place.location_url,
        history=place.history,
        url_img=place.url_img,
        found_number=place.found_number
    )


def validate_place(place: PlaceCreate) -> bool:
    patron_location_url = re.compile(r'^https://maps\.app\.goo\.gl/[A-Za-z0-9]+$')
    patron_url_img = re.compile(r'^(https?|ftp)://[^\s/$.?#].[^\s]*$')
    
    if not patron_location_url.match(place.location_url):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid location url",
        )
    
    if not patron_url_img.match(place.url_img):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid url image",
        )


def get_place_service(db: Session, place_id: int) -> Place:
    Find_Place = db.query(PlaceModel).filter(PlaceModel.id == place_id).first()
    if Find_Place is None:
        return None
    else:
        return transform_place_to_place_schema(Find_Place)
    

def get_place_by_uuid_service(db: Session, place_uuid: str) -> Place:
    Find_Place = db.query(PlaceModel).filter(PlaceModel.uuid == place_uuid).first()
    if Find_Place is None:
        return None
    else:
        return transform_place_to_place_schema(Find_Place)


def get_places_service(db: Session, skip: int = 0, limit: int = 100) -> listPlace:
    places = db.query(PlaceModel).offset(skip).limit(limit).all()
    
    result_places = [
        transform_place_to_place_schema(place) for place in places
    ]
    return listPlace(places=result_places)


def create_place_service(db: Session, place: PlaceCreate) -> Place:
    validate_place(place)
    
    db_place = PlaceModel(name=place.name, city=place.city, 
                        location_url=place.location_url, 
                        history=place.history, url_img=place.url_img, 
                        found_number=place.found_number)
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return transform_place_to_place_schema(db_place)


def delete_place_service(db: Session, place_id: int) -> Place:
    db_place = db.query(PlaceModel).filter(PlaceModel.id == place_id).first()
    if db_place is None:
        return None
    db.delete(db_place)
    db.commit()
    return transform_place_to_place_schema(db_place)