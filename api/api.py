from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.base import SessionLocal
from app.repository.repo import create_road_data
from app.schemas.schema import StreetViewSchema
from datetime import datetime

current_time = datetime.now()
print(current_time)


router = APIRouter()
repository = create_road_data(StreetViewSchema, Session)


@router.post("/streetview/", response_model=StreetViewSchema)
def create_road_data(data: StreetViewSchema):
    return repository.create_road_data(data.dict())


@router.get("/streetview/", response_model=StreetViewSchema)
def get_road_data():
    result = repository.get_road_data_by_camera_and_time()
    if not result:
        raise HTTPException(status_code=404, detail="Data not found")
    return result


@router.get("/streetview/{camera}/{time}", response_model=StreetViewSchema)
def get_road_data_by_camera_and_time(camera: int, time: datetime):
    result = repository.get_road_data_by_camera_and_time(camera, time)
    if not result:
        raise HTTPException(status_code=404, detail="Data not found")
    return result


@router.put("/streetview/{id}", response_model=StreetViewSchema)
def update_road_data(id: int, data: StreetViewSchema):
    db_data = repository.get_road_data_by_id(id)
    if not db_data:
        raise HTTPException(status_code=404, detail="Data not found")

    for field, value in data.dict().items():
        setattr(db_data, field, value)
    return db_data
