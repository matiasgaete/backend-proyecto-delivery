import repositorioUsuario as rpU
from sqlalchemy.exc import IntegrityError


def crear_usuario_service(user):
    try:
        rpU.crear_usuario_repo(user)
    except IntegrityError as e:
        print("Nombre de la clase:", type(e).__name__)
    return

def iniciar_sesion_service(credenciales):
    resultado = rpU.inicar_sesion_repo(credenciales)
    return resultado

def cambiar_pass_service(credenciales):
    resultado = rpU.cambiar_pass_repo(credenciales)
    return

def solicitar_cambio_service(email):
    resultado = rpU.solicitar_cambio_repo(email)
    if resultado is None:
        return "No existe ese usuario"
    return resultado
    
