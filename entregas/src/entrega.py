from sqlalchemy import String, Integer, DateTime, func
from sqlalchemy.orm import DeclarativeBase, mapped_column

class Base(DeclarativeBase):
    pass

class Entrega(DeclarativeBase):
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    hora_aceptacion = mapped_column(DateTime, nullable=False)
    hora_recogida = mapped_column(DateTime, nullable=False)
    hora_entrega  = mapped_column(DateTime, nullable=False)
    monto = mapped_column(Integer, nullable=False)
    id_local = mapped_column(Integer, nullable=False)
    app = mapped_column(String, nullable=False)