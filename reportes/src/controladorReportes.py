from fastapi import APIRouter
from pydantic import BaseModel
from serviceReportes import *


router = APIRouter(prefix="/reportes")


class agregarReporteDTO(BaseModel):
    nombre_local: str
    direccion: str
    long: float
    lat: float
    titulo_reporte: str
    descripcion_reporte: str


class agregarValidacionDTO(BaseModel):
    id_local: int
    valido: bool


@router.post("/agregar-reporte")
def agregar_reporte_controler(reporte: agregarReporteDTO):
    return agregar_reporte_service(reporte)


@router.get("/consultar-reportes")
def consultar_reportes_controler(lat: float, long: float, radio: float):
    return consultar_reportes_service(lat, long, radio)


@router.post("/agregar-validacion")
def agregar_validacion_controler(validacion: agregarValidacionDTO):
    return agregar_validacion_service(validacion)
