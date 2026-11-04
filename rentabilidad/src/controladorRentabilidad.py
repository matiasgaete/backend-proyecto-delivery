from fastapi import APIRouter
import serviceRentabilidad as sR
from pydantic import BaseModel


router = APIRouter(prefix="/rentabilidad")

class buscarLocalesDTO(BaseModel):
    lat: float
    long: float
    radio: float

@router.get("/locales")
def calcular_rentabilidad_controller(area: buscarLocalesDTO):
    sR.calcular_rentabilidad_service(area)

