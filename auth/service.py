from cliente import *
from fastapi import HTTPException

async def service_validar_credenciales(credenciales):
    resultado = await consultar_credenciales(credenciales)
    if resultado.status_code != 200:
        raise HTTPException(
            status_code = resultado.status_code,
            detail = "Error en la autenticacion"
        )
    else:
        payload = {}
        

    return resultado.json()