from fastapi import APIRouter, Depends
import serviceLocales as sLo
from security import validar_token

router = APIRouter(
    prefix="/locales",
    dependencies=[Depends(validar_token)]
    )

@router.get("/consultar-locales")
def consultar_locales_controller(radio: float, long: float, lat: float):
    return sLo.consultar_locales_service(radio, long, lat)
