from sqlalchemy import Boolean, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase, mapped_column
from bd import Base

class Validacion(Base):
    __tablename__ = "validaciones"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    valido = mapped_column(Boolean, nullable=False)
    id_reporte = mapped_column(
        Integer,
        ForeignKey("reportes_locales.id", ondelete="CASCADE"),
        nullable=False,
    )