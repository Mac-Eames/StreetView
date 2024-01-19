
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
import os
from sqlalchemy.orm import sessionmaker

# Class to get the postgresql details


class Settings:
    PROJECT_NAME: str = "Google Street View App"
    PROJEVT_VERSION: str = "1.0.0"

    POSTGRES_USER: str = os.getenv('postgres')
    POSTGRES_PASSWORD = os.getenv("@Habeeb123")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", 'localhost')
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "Google streetview")

    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"


settings = Settings()

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

metadata = MetaData()

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base = declarative_base()
