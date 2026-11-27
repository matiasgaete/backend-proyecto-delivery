from datetime import datetime
from fastapi import APIRouter, Depends
import serviceRentabilidad as sR
from security import validar_token


router = APIRouter(
    prefix="/rentabilidad"
    )

@router.get("/locales")
async def calcular_rentabilidad_controller(
    lat: float, 
    long: float, 
    radio: float, 
    hora_peticion: datetime,
    app: str = "",
    token: dict = Depends(validar_token)
    ):
    return await sR.calcular_rentabilidad_service(
        lat, long, radio, hora_peticion, app, token
    )
