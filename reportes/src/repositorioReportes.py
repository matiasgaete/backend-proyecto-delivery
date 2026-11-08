from bd import config
from geoalchemy2 import Geography
from sqlalchemy import func
from sqlalchemy import select
from reporte import *
from validacion import *


def consultar_reportes_repo(lat, long, radio):
    with config() as session:
        query = select(ReporteLocal).where(
            func.ST_DWithin(
                ReporteLocal.ubicacion,
                func.ST_SetSRID(func.ST_MakePoint(long, lat), 4326),
                radio
            )
        )
        return session.scalars(query).all()


def agregar_reporte_repo(reporte):
    with config() as session:
        nuevo_reporte = ReporteLocal(
            nombre_local=reporte.nombre_local,
            direccion=reporte.direccion,
            ubicacion=func.ST_SetSRID(func.ST_MakePoint(reporte.long, reporte.lat), 4326),
            titulo_reporte=reporte.titulo_reporte,
            descripcion_reporte=reporte.descripcion_reporte,
        )

        session.add(nuevo_reporte)
        session.commit()

        return nuevo_reporte


def agregar_validacion_repo(validacion):
    with config() as session:
        nueva_validacion = Validacion(
            id_reporte=validacion.id_local,
            valido=validacion.valido,
        )
        session.add(nueva_validacion)
        session.commit()
        session.refresh(nueva_validacion)

        return {
            "id": nueva_validacion.id,
            "id_reporte": nueva_validacion.id_reporte,
            "valido": nueva_validacion.valido,
        }