from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

ENV_FILE = Path(__file__).resolve().parent.parent / ".env" 

class Settings(BaseSettings):
    DATABASE_URL: str
    model_config = SettingsConfigDict(env_file=ENV_FILE, end_file_encoding="uft-8")

settings = Settings()
engine = create_engine(settings.DATABASE_URL)
config = sessionmaker(bind=engine, autocommit=False, autoflush=False)
