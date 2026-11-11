from fastapi import APIRouter
import serviceRentabilidad as sR


router = APIRouter(prefix="/rentabilidad")

@router.get("/locales")
async def calcular_rentabilidad_controller(lat: float, long: float, radio: float, app: str = ""):
    return await sR.calcular_rentabilidad_service(lat, long, radio, app)
