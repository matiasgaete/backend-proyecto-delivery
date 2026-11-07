from repositoryEntregas import *


def get_entregas_service(condiciones):
    resultados_json = {"items": []}
    entregas = get_entregas_repo(condiciones)
    for entrega in entregas:
        rango_horario = (entrega.hora_entrega - entrega.hora_aceptacion) / 60
        resultados_json["items"].append(
            {
                "id": entrega.id,
                "rango_horario": rango_horario,
                "monto": entrega.monto
            }
        )
    return resultados_json

