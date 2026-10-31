from fastapi import APIRouter
import serviceRentabilidad as sR
from pydantic import BaseModel


router = APIRouter(prefix="/rentabilidad")

class buscarLocalesDTO(BaseModel):
    lat: float
    long: float
    radio: float

@router.get("/locales")
def buscar_locales_controller(area: buscarLocalesDTO):
    sR.buscar_locales_service(area)

    