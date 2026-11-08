from fastapi import APIRouter, Depends, Query
from datetime import datetime
from pydantic import BaseModel, Field
from serviceEntregas import *

router = APIRouter(prefix="/entregas")

class getEntregasDTO(BaseModel):
    ids_locales: list[int] = Field(Query(...))
    hora_peticion: datetime 

class agregarEntregasDTO(BaseModel):
    hora_aceptacion: datetime
    hora_recogida: datetime
    hora_entrega: datetime
    monto: int
    id_local: int
    app: str

@router.get("/entregas-id")
def get_entregas_controller(condiciones: getEntregasDTO = Depends()):
    return get_entregas_service(condiciones)

@router.post("/agregar-entrega")
def agregar_entrega_controller(entrega: agregarEntregasDTO):
    return agregar_entrega_service(entrega)