from sqlalchemy.orm import Session
from app.models.models import Road
from app.schemas.schema import StreetViewSchema
from shapely.geometry import LineString 

def create_road_data(request: StreetViewSchema, db: Session):
    road_geom = f"LINESTRING({', '.join([f'{x} {y}' for x, y in request.geometry])})"
    db_road_data = Road(
            geometry = road_geom,
        )
    db.add(db_road_data)
    db.commit()
    db.refresh(db_road_data)
    return "Line data created successfully"


