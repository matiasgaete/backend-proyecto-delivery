from geoalchemy2 import Geography
from sqlalchemy import Integer, String, Text, TIMESTAMP, func
from sqlalchemy.orm import DeclarativeBase, mapped_column
from bd import Base


class ReporteLocal(Base):
    __tablename__ = "reportes_locales"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre_local = mapped_column(String(255), nullable=False)
    direccion = mapped_column(Text, nullable=False)
    ubicacion = mapped_column(
        Geography(geometry_type="POINT", srid=4326),
        nullable=False,
    )
    titulo_reporte = mapped_column(String(255), nullable=False)
    descripcion_reporte = mapped_column(Text)
    creado_en = mapped_column(TIMESTAMP, server_default=func.current_timestamp())
