from fastapi import APIRouter
import serviceRentabilidad as sR
from pydantic import BaseModel


router = APIRouter(prefix="/rentabilidad")

class buscarLocalesDTO(BaseModel):
    lat: float
    long: float
    radio: float

@router.get("/locales")
async def calcular_rentabilidad_controller(lat: float, long: float, radio: float):
    return await sR.calcular_rentabilidad_service(lat, long, radio)

