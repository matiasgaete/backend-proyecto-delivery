from fastapi import Router
import serviceLocales as sLo

router = Router(prefix="/locales")

@router.get("/consultar-locales")
def consultar_locales_controller(radio: float, long: float, lat: float):
    sLo.consultar_locales_service(radio, long, lat)