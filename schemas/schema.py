from pydantic import BaseModel
from geojson_pydantic.features import Feature
from datetime import datetime
from typing import List, Tuple



class StreetViewCreate(BaseModel):
    geometry: List[List[float]]
    camera: int

class StreetViewUpdate(BaseModel):
    geometry: List[List[float]]
    camera: int

class StreetViewSchema(BaseModel):
    id: int
    geometry: List[List[float]]
    distance: float
    time: datetime
    camera: int


    class Config:
        orm_mode = True

    
