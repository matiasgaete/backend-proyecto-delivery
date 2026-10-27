from bd import config
from usuario import Usuario
from sqlalchemy import select, or_, update

def crear_usuario_repo(user):
    with config() as session:
        # Usuario(nombre_atributo_clase=1"valor", nombre_atributo_clase2="valor")
        nuevo_usuario = Usuario(nombre=user.nombre,
                                apellido=user.apellido,
                                rut=user.rut,
                                correo=user.correo,
                                password_hash=user.password)
        
        session.add(nuevo_usuario)
        session.commit()
    return

def consultar_usuario_repo(correo, rut):
    with config() as session:
        query = select(Usuario).where(
            or_(
                correo == Usuario.correo,
                rut == Usuario.rut
                )
            )
        resultado = session.scalars(query)
        return resultado.one_or_none()

def cambiar_pass_repo(credenciales):
    with config() as session:
        query = (
            update(Usuario)
            .where(credenciales.correo == Usuario.correo)
            .values(password_hash=credenciales.new_pass)
            )

        resultado = session.execute(query)
        session.commit()
        return
    