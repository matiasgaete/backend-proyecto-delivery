from repositorioReportes import *
from geoalchemy2.shape import to_shape
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status


def agregar_reporte_service(reporte):
    try:
        agregar_reporte_repo(reporte)
        return {"message": "Reporte creado con exito"}
    except IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error en el formato de entrada"
        )
    

def agregar_validacion_service(validacion):
    try:
        agregar_validacion_repo(validacion)
        return {"message": "Validacion agregada con exito"}
    except IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reporte no existente"
        )
    


def consultar_reportes_service(lat, long, radio):
    resultados_json = {"items": []}
    resultado = reportes = consultar_reportes_repo(lat, long, radio)
    for reporte in resultado:
        punto = to_shape(reporte.ubicacion)
        resultados_json["items"].append(
            {
                "id": reporte.id,
                "nombre_local": reporte.nombre_local,
                "direccion": reporte.direccion,
                "titulo_reporte": reporte.titulo_reporte,
                "descripcion_reporte": reporte.descripcion_reporte,
                "creado_en": reporte.creado_en,
                "long": punto.x,
                "lat": punto.y
            }
        )
    return resultados_json
