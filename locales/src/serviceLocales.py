from repositoryLocales import *


def consultar_locales_service(radio, long, lat):
    resultados_json = {"items": []}
    resultado = consultar_locales_repo(radio, long, lat)
    for local in resultado:
        id = local.id
        nombre = local.nombre
        direccion = local.direccion
        resultados_json["items"].append(
            {
                "id": id,
                "nombre": nombre,
                "direccion": direccion 
            }
        )
    return resultados_json
