import repositorioUsuario as rpU
import resend
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status


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
    resultado = rpU.cambiar_pass_repo(credenciales)
    if resultado:
        return {"message": "Contraseña actualizada exitosamente"}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

def solicitar_cambio_service(email):
    resultado = rpU.solicitar_cambio_repo(email)
    if resultado is None:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    else:
        resend.api_key = "re_f2fzgdN7_8yNha8T6Uf1cB9t2KVZAa4zh"

        r = resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": f"{resultado.correo}",
        "subject": "Restablecer contraseña",
        "html": "<p>Haz clic <a href='http://127.0.0.1:8000/docs#/default/cambiar_pass_controler_usuarios_cambiar_pass_put'>aquí</a> para cambiar tu clave.</p>"
        })

        return {"exito": True, "email": resultado.correo}
