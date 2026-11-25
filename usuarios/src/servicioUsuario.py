import repositorioUsuario as rpU
import resend
import hashlib
import logging
import secrets
from datetime import datetime, timedelta, timezone
from config import settings
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

logger = logging.getLogger(__name__)

def consultar_id_service(id):
    resultado = rpU.consultar_id_repo(id)
    if resultado:
        return resultado
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

def crear_usuario_service(user):
    try:
        rpU.crear_usuario_repo(user)
        return {"message": "Usuario creado con exito"}
    except IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El usuario ya se encuentra registrado"
        )

def iniciar_sesion_service(credenciales):
    resultado = rpU.inicar_sesion_repo(credenciales)
    if resultado is None:
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas"
        )
    
    return resultado

def cambiar_pass_service(credenciales):
    token_hash = hashlib.sha256(credenciales.token.encode("utf-8")).hexdigest()
    resultado = rpU.cambiar_pass_repo(
        credenciales.correo,
        token_hash,
        credenciales.new_pass,
    )
    if resultado:
        return {"message": "Contraseña actualizada exitosamente"}
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Token inválido o expirado"
        )

def solicitar_cambio_service(email):
    resultado = rpU.solicitar_cambio_repo(email)
    if resultado is None:
        return {
            "exito": True,
            "message": "Si el correo está registrado, recibirás un enlace para restablecer la contraseña",
        }

    token = secrets.token_urlsafe(32)
    token_hash = hashlib.sha256(token.encode("utf-8")).hexdigest()
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=30)

    if not rpU.guardar_token_restablecimiento_repo(email, token_hash, expires_at):
        return {
            "exito": True,
            "message": "Si el correo está registrado, recibirás un enlace para restablecer la contraseña",
        }

    reset_url = f"http://localhost:5173/?token={token}"
    resend.api_key = settings.API_KEY
    try:
        resend.Emails.send(
            {
                "from": "onboarding@resend.dev",
                "to": resultado.correo,
                "subject": "Restablecer contraseña",
                "html": (
                    "<p>Para restablecer tu contraseña, haz clic en este enlace:</p>"
                    f"<p><a href='{reset_url}'>Restablecer contraseña</a></p>"
                    "<p>El enlace vence en 30 minutos y solo puede usarse una vez.</p>"
                ),
            }
        )
    except Exception as error:
        rpU.invalidar_token_restablecimiento_repo(token_hash)
        logger.exception("No se pudo enviar el correo de restablecimiento")
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="No se pudo enviar el correo de restablecimiento",
        ) from error

    return {
        "exito": True,
        "message": "Si el correo está registrado, recibirás un enlace para restablecer la contraseña",
    }
