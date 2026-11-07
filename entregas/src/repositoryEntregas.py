from entrega import Entrega
from sqlalchemy import select, and_
from bd import config
from datetime import timedelta

def get_entregas_repo(condiciones):
    with config() as session:
        margen = timedelta(minutes=15)
        limite_inferior = condiciones.hora_peticion - margen
        limite_superior = condiciones.hora_peticion + margen

        query = select(Entrega).where(
            and_(
                Entrega.id_local.in_(condiciones.ids_locales),
                Entrega.hora_recogida >= limite_inferior,
                Entrega.hora_recogida <= limite_superior
            )   
        )

        entregas = session.scalars(query).all()
        return entregas
