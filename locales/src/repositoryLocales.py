from bd import config
from sqlalchemy import select, func
from local import Local

def consultar_locales_repo(radio, long, lat):
    with config() as session:
        query = select(Local).where(
            # Funcion postgre para calcuar ubicaciones en un radio
            # (punto A, punto B, Radio)
            func.ST_DWithin(
                Local.ubicacion,
                # funcion postgre para definir una ubicacion
                func.ST_SetSRID(func.ST_MakePoint(long, lat), 4326),
                radio
                )
        )
        #retorna lista con objetos Local
        locales = session.scalars(query).all()
        return locales
