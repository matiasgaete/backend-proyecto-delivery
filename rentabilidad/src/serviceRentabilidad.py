import clienteEntregas as clE
import clienteLocales as clL
from collections import defaultdict

async def calcular_rentabilidad_service(lat, long, radio, app):
    locales = await clL.consultar_locales(lat, long, radio)
    items_locales = locales.get("items", [])
    if not items_locales:
        return locales

    id_locales = [local["id"] for local in items_locales]
    entregas = await clE.consultar_entregas(id_locales, app)

    acumulado = defaultdict(lambda: {"rentabilidad_sum": 0.0, "cantidad": 0})
    for item in entregas.get("items", []):
        local_id = item["id"]
        if item["rango_horario"] == 0:
            continue
        acumulado[local_id]["rentabilidad_sum"] += item["monto"] / item["rango_horario"]
        acumulado[local_id]["cantidad"] += 1

    items_resultado = []
    for local in items_locales:
        local_id = local["id"]
        datos = acumulado[local_id]
        if datos["cantidad"] == 0:
            continue
        
        rentabilidad = (datos["rentabilidad_sum"] / datos["cantidad"])
        
        item_nuevo = local.copy()
        item_nuevo["rentabilidad"] = rentabilidad
        item_nuevo["fiable"] = datos["cantidad"] > 3
        items_resultado.append(item_nuevo)

    items_resultado.sort(key=lambda x: x["rentabilidad"], reverse=True)

    resultado = locales.copy()
    resultado["items"] = items_resultado
    return resultado