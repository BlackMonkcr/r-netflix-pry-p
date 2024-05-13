from pydantic import BaseModel
from typing import List

# Place schemas

class PlaceBase(BaseModel):
    name: str
    city: str
    location_url: str
    history: str
    url_img: str
    found_number: int = 0

class PlaceCreate(PlaceBase):
    pass

class Place(PlaceBase):
    id: int

    class Config:
        from_attributes = True

class Place_blocked(Place):
    is_blocked: bool = True

    class Config:
        from_attributes = True

class listPlace(BaseModel):
    places: List[Place]

    class config:
        from_attributes = True

class listPlace_blocked(BaseModel):
    places: List[Place_blocked]

    class config:
        from_attributes = True
