from fastapi import APIRouter, Depends, Query
from datetime import datetime
from pydantic import BaseModel, Field
from serviceEntregas import *

router = APIRouter(prefix="/entregas")

class getEntregasDTO(BaseModel):
    ids_locales: list[int] = Field(Query(...))
    hora_peticion: datetime 

@router.get("/entregas-id")
def get_entregas_controller(condiciones: getEntregasDTO = Depends()):
    return get_entregas_service(condiciones)
