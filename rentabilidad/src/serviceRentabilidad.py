import httpx


def buscar_locales_service(area):
    respuesta = httpx.AsyncClien.get("url")
    return respuesta.json