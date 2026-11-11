from sqlalchemy import String, Integer, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass

class Entrega(Base):
    __tablename__ = "entregas"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    hora_aceptacion = mapped_column(TIMESTAMP(timezone=True), nullable=False)
    hora_recogida = mapped_column(TIMESTAMP(timezone=True), nullable=False)
    hora_entrega  = mapped_column(TIMESTAMP(timezone=True), nullable=False)
    monto = mapped_column(Integer, nullable=False)
    id_local = mapped_column(Integer, nullable=False)
    app = mapped_column(String(50), nullable=False)
    