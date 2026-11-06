from fastapi import APIRouter
import serviceLocales as sLo

router = APIRouter(prefix="/locales")

@router.get("/consultar-locales")
def consultar_locales_controller(radio: float, long: float, lat: float):
    return sLo.consultar_locales_service(radio, long, lat)
