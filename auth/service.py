from cliente import *
from fastapi import HTTPException
from datetime import datetime, timezone, timedelta
import jwt
import secrets
from repoAuth import (
    create_update_sesion,
    get_sesion_dispositivo_token,
    eliminar_sesion_repo
)

def create_refresh_token(dias_validez: int = 30) -> tuple[str, datetime]:
    refresh_token = secrets.token_urlsafe(48)
    vencimiento = datetime.now(timezone.utc) + timedelta(days=dias_validez)
    return refresh_token, vencimiento


def create_access_token(payload):
    with open("private_key.pem", "rb") as file:
        private_key = file.read()

    return jwt.encode(payload, private_key, algorithm="ES256")


def obtener_usuario(resultado):
    if resultado.status_code != 200:
        raise HTTPException(
            status_code=resultado.status_code,
            detail="Error en la autenticacion",
        )
    return resultado.json()


def crear_payload_usuario(usuario):
    hora_peticion = datetime.now(timezone.utc)
    duracion = timedelta(minutes=0.25)

    return {
        "sub": f"{usuario["id"]}",
        "exp": hora_peticion + duracion,
        "iat": hora_peticion,
        "nombre": usuario["nombre"],
        "apellido": usuario["apellido"],
        "rut": usuario["rut"],
        "correo": usuario["correo"],
    }


async def validar_credenciales(credenciales):
    resultado = await consultar_credenciales(credenciales)
    usuario = obtener_usuario(resultado)
    return crear_payload_usuario(usuario)


async def login_service(credenciales):
    payload = await validar_credenciales(credenciales)
    access_token = create_access_token(payload)
    refresh_token, vencimiento = create_refresh_token()

    payload = jwt.decode(
        access_token,
        options={"verify_signature": False}
    )

    create_update_sesion(
        int(payload["sub"]),
        credenciales.device_id,
        refresh_token,
        vencimiento)

    return {"acces_token": access_token,
            "refresh_token": refresh_token}


async def refrescar_token(device_id, refresh_token):
    sesion = get_sesion_dispositivo_token(device_id, refresh_token)
    if sesion is None or sesion.expires_at <= datetime.now(timezone.utc):
        raise HTTPException(
            status_code=401,
            detail="Refresh token invalido, expirado o asociado a otro dispositivo",
        )

    resultado = await consultar_id(sesion.user_id)
    usuario = obtener_usuario(resultado)
    payload = crear_payload_usuario(usuario)
    access_token = create_access_token(payload)
    nuevo_refresh_token, vencimiento = create_refresh_token()

    create_update_sesion(
        sesion.user_id,
        device_id,
        nuevo_refresh_token,
        vencimiento,
    )

    return {
        "acces_token": access_token,
        "refresh_token": nuevo_refresh_token,
    }


def logout_service(device_id, refresh_token):
    sesion = get_sesion_dispositivo_token(device_id, refresh_token)
    if sesion is None:
        raise HTTPException(
            status_code=401,
            detail="Refresh token invalido o asociado a otro dispositivo",
        )

    eliminar_sesion_repo(sesion.user_id, device_id)
    return {"message": "Sesion cerrada"}
