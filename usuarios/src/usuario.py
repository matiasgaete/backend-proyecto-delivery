from sqlalchemy import Integer, String, DateTime, func
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass

class Usuario(Base):
    # nombre de la tabla de la bd a la q corresponde
    __tablename__ = "usuarios"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre = mapped_column(String(100), nullable=False)
    apellido = mapped_column(String(100), nullable=False)
    rut = mapped_column(String(12), unique=True, nullable=False)
    correo = mapped_column(String(150), unique=True, nullable=False)
    password_hash = mapped_column(String(255), nullable=False)
    creado_en = mapped_column(DateTime, server_default=func.now())
        