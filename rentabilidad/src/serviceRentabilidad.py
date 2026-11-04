import httpx


def calcular_rentabilidad_service(area):
    respuesta_locales = httpx.AsyncClien.get("url")
    dic_locales = respuesta_locales.json()
    id = dic_locales["id"]
    nombre = dic_locales["nombre"]

    respuesta_entregas = httpx.AsyncClent.get("url")
    dic_entregas = respuesta_entregas.json()
    id = dic_entregas["id"]
    rentabilidad_promedio = dic_entregas["promedio"]
    