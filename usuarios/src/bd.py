from config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(settings.DATABASE_URL)
conf = sessionmaker(bind=engine, autocommit=False, autoflush=False)