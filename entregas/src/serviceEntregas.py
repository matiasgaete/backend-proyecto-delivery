from repositoryEntregas import *
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status


def get_entregas_service(condiciones):
    resultados_json = {"items": []}
    entregas = get_entregas_repo(condiciones)
    for entrega in entregas:
        rango_horario = (entrega.hora_entrega - entrega.hora_aceptacion) / 60
        resultados_json["items"].append(
            {
                "id": entrega.id_local,
                "rango_horario": rango_horario,
                "monto": entrega.monto
            }
        )
    return resultados_json

def agregar_entrega_service(entrega):
    try:
        agregar_entrega_repo(entrega)
        return {"message": "Entrega registrada con exito"}
    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error el registrar la entrega"
        )


