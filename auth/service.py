from cliente import *
from fastapi import HTTPException
from datetime import datetime, timezone, timedelta
import jwt

async def service_validar_credenciales(credenciales):
    resultado = await consultar_credenciales(credenciales)
    if resultado.status_code != 200:
        raise HTTPException(
            status_code = resultado.status_code,
            detail = "Error en la autenticacion"
        )
    else:
        usuario = resultado.json()

        hora_peticion = datetime.now(timezone.utc)
        duracion = timedelta(minutes=15)

        payload = {
            "sub": f"{usuario["id"]}",
            "exp": hora_peticion + duracion,
            "iat":hora_peticion,
            "nombre": usuario["nombre"],
            "apellido": usuario["apellido"],
            "rut": usuario["rut"],
            "correo": usuario["correo"]
            }
        
        with open("private_key.pem", "rb") as file:
            private_key = file.read()

        try:
            algorithm = "ES256"
            token_auth = jwt.encode(payload, private_key, algorithm)
            return token_auth

        except:
            return "error"
            