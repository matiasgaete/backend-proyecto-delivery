from fastapi import APIRouter, Depends
from datetime import datetime
from pydantic import BaseModel
from serviceEntregas import *

router = APIRouter(prefix="/entregas")

class getEntregasDTO(BaseModel):
    id_local: int
    hora_peticion: datetime 

@router.get("/entregas-id")
def get_entregas_controller(condiciones: getEntregasDTO = Depends()):
    get_entregas_service(condiciones)