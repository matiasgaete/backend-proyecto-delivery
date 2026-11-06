from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, mapped_column
from geoalchemy2 import Geography

class Base(DeclarativeBase):
    pass

class Local(Base):
    __tablename__ = "locales"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre = mapped_column(String(150), nullable=False)
    direccion = mapped_column(String(250))
    ubicacion = mapped_column(Geography(geometry_type="POINT", srid=4326))
