import httpx
import clienteEntregas as clE
import clienteLocales as clL
from rentabilidades import *

async def calcular_rentabilidad_service(lat, long, radio):
    locales = await clL.consultar_locales(lat, long, radio)
    id_locales = []
    for local in locales["items"]:
        id_locales.append(local["id"])

    entregas = await clE.consultar_entregas(id_locales)

    rentabilidad = {}
    for item in entregas["items"]:
        if item["id"] in rentabilidad:
            rentabilidad[item["id"]][0] += item["monto"]
            rentabilidad[item["id"]][1] += item["rango_horario"]
        else:
            rentabilidad[item["id"]] = [item["monto"], item["rango_horario"]]

    for clave in rentabilidad:
        rentabilidad[clave] = rentabilidad[clave][0] / rentabilidad[clave][1]

    datos_rentabilidad = locales.copy()
    for dato in datos_rentabilidad["items"]:
        dato["rentabilidad"] = rentabilidad[dato["id"]]

    datos_rentabilidad["items"] = sorted(
        datos_rentabilidad["items"],
        key=lambda x: x["rentabilidad"],
        reverse=True
        )

    return datos_rentabilidad
