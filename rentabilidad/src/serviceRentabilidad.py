import httpx
import clienteEntregas as clE
import clienteLocales as clL
from rentabilidades import *

async def calcular_rentabilidad_service(lat, long, radio):
    locales = await clL.consultar_locales(lat, long, radio)
    obj_rentabilidades = []
    for local in locales["items"]:
        obj = Rentabilidad(local["id"], local["nombre"])
        obj_rentabilidades.append({local["id"]: obj})

    entregas = await clE.consultar_entregas(id_locales)
    
    for id in id_locales:
        for entrega in entregas["items"]:
            if id == entrega["id"]:
                rentabilidad.append(
                    {

                    }
                )


        
    