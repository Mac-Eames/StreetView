from sqlalchemy import Column, Integer, DateTime, Float
from geoalchemy2 import Geometry
from app.db.base import Base

class Road(Base):
    __tablename__ = "road_data"

    id = Column(Integer, primary_key=True, index=True)
    geometry = Column(Geometry(geometry_type="LINESTRING", srid=4326))
    distance = Column(Float)
    time = Column(DateTime)
    camera = Column(Integer) 

