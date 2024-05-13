from sqlalchemy.orm import Session
from domain.models import User as UserModel
from domain.models import Place as PlaceModel
from domain.models import User as UserModel
from domain.dtos.place_schemas import Place, Place_blocked, listPlace_blocked
from domain.models import collectable
from datetime import datetime, timedelta
from fastapi import HTTPException, status


def get_places_of_user_service(db: Session, user_id: int) -> listPlace_blocked:
    Find_User = db.query(UserModel).filter(UserModel.id == user_id).first()
    Find_Places = db.query(PlaceModel).all()
    if Find_User is None:
        return None
    else:
        places = []
        for place in Find_Places:
            if place in Find_User.places:
                places.append(Place_blocked(is_blocked=False, **place.__dict__))
            else:
                places.append(Place_blocked(is_blocked=True, **place.__dict__))
        return listPlace_blocked(places=places)
    

def add_place_to_user_service(db: Session, user_id: int, place_id: int) -> Place:
    Find_User = db.query(UserModel).filter(UserModel.id == user_id).first()
    Find_Place = db.query(PlaceModel).filter(PlaceModel.id == place_id).first()
    if Find_User is None or Find_Place is None:
        return None
    else:
        if Find_Place not in Find_User.places:
            Find_User.number_places_visited += 1
            Find_Place.found_number += 1
            db.execute(
                collectable.insert().values(
                    user_id=user_id,
                    place_id=place_id,
                    date=datetime.now(),
                    position_found=Find_Place.found_number,
                    number_visited=1
                )
            )
        
        else:
            collectable_record = db.query(collectable).filter(
                collectable.c.user_id == user_id,
                collectable.c.place_id == place_id
            ).first()

            last_visited_date = collectable_record.date
            current_date = datetime.now()

            if current_date - last_visited_date >= timedelta(days=1):
                db.execute(
                    collectable.update().where(
                        collectable.c.user_id == user_id and collectable.c.place_id == place_id
                    ).values(
                        date=datetime.now(),
                        number_visited=collectable.c.number_visited + 1
                    )
                )
                db.commit()
                db.refresh(collectable_record)
            else:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Place visited in the last 24 hours.",
                )

        db.commit()
        db.refresh(Find_User)
        db.refresh(Find_Place)
        return Place(**Find_Place.__dict__)
    

def add_place_to_user_service_uuid(db: Session, user_id: int, place_uuid: str) -> Place:
    Find_User = db.query(UserModel).filter(UserModel.id == user_id).first()
    Find_Place = db.query(PlaceModel).filter(PlaceModel.uuid == place_uuid).first()
    if Find_User is None or Find_Place is None:
        return None
    else:
        if Find_Place not in Find_User.places:
            Find_User.number_places_visited += 1
            Find_Place.found_number += 1
            db.execute(
                collectable.insert().values(
                    user_id=user_id,
                    place_id=Find_Place.id,
                    date=datetime.now(),
                    position_found=Find_Place.found_number,
                    number_visited=1
                )
            )
        
        else:
            collectable_record = db.query(collectable).filter(
                collectable.c.user_id == user_id,
                collectable.c.place_id == Find_Place.id
            ).first()

            last_visited_date = collectable_record.date
            current_date = datetime.now()

            if current_date - last_visited_date >= timedelta(days=1):
                db.execute(
                    collectable.update().where(
                        collectable.c.user_id == user_id and collectable.c.place_id == Find_Place.id
                    ).values(
                        date=datetime.now(),
                        number_visited=collectable.c.number_visited + 1
                    )
                )
                db.commit()
                db.refresh(collectable_record)
            else:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Place visited in the last 24 hours.",
                )

        db.commit()
        db.refresh(Find_User)
        db.refresh(Find_Place)
        return Place(**Find_Place.__dict__)