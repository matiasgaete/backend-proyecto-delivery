from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

ENV_FILE = Path(__file__).resolve().parent.parent / ".env" 

class Settings(BaseSettings):
    DATABASE_URL: str
    API_KEY: str
    model_config = SettingsConfigDict(env_file=ENV_FILE, end_file_encoding="uft-8")

settings = Settings()

with open("public_key.pem", "rb") as file:
    public_key = file.read()