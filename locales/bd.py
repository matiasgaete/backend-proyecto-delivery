from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


## ajustar bd
url = "postgresql://postgres:Matiasgaete1@localhost:5432/proyectoDelivery"
engine = create_engine(url)

config = sessionmaker(bind=engine, autocommit=False, autoflush=False)
