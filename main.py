from fastapi import FastAPI
from app.api.api import router as geospatial_router

app = FastAPI()

app.include_router(geospatial_router)



