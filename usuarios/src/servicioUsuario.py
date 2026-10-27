import repositorioUsuario as rpU
from sqlalchemy.exc import IntegrityError


def crear_usuario_service(user):
    try:
        rpU.crear_usuario_repo(user)
    except IntegrityError as e:
        print("Nombre de la clase:", type(e).__name__)
    return

def consultar_usuario_service(correo, rut):
    resultado = rpU.consultar_usuario_repo(correo, rut)
    return resultado

def cambiar_pass_service(credenciales):
    resultado = rpU.cambiar_pass_repo(credenciales)
    return
