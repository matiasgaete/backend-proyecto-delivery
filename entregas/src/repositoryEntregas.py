from entrega import Entrega
from sqlalchemy import select, and_, or_
from bd import config
from datetime import timedelta

def get_entregas_repo(condiciones):
    with config() as session:
        margen = timedelta(minutes=30)
        limite_inferior = condiciones.hora_peticion - margen
        limite_superior = condiciones.hora_peticion

        query = select(Entrega).where(
            and_(
                Entrega.id_local.in_(condiciones.ids_locales),
                Entrega.hora_entrega >= limite_inferior,
                Entrega.hora_entrega <= limite_superior,
                or_(
                    condiciones.app == "",
                    Entrega.app == condiciones.app
                )
            )   
        )

        entregas = session.scalars(query).all()
        return entregas

def agregar_entrega_repo(entrega):
    with config() as session:
        new_entrega = Entrega(
            hora_aceptacion=entrega.hora_aceptacion,
            hora_recogida=entrega.hora_recogida,
            hora_entrega=entrega.hora_entrega,
            monto=entrega.monto,
            id_local=entrega.id_local,
            app=entrega.app
        )

        session.add(new_entrega)
        session.commit()
    return
    