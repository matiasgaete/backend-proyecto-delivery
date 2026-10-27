from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

url = "postgresql://postgres:Matiasgaete1@localhost:5432/proyectoDelivery"
engine = create_engine(url)

config = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    