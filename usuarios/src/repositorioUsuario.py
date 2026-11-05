from bd import config
from usuario import Usuario
from sqlalchemy import select, and_, update

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

def inicar_sesion_repo(credenciales):
    with config() as session:
        query = select(Usuario).where(
            and_(
                credenciales.correo == Usuario.correo,
                credenciales.password == Usuario.password_hash
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

        session.execute(query)
        session.commit()
        return

def solicitar_cambio_repo(email):
    with config() as session:
        query = select(Usuario).where(
            Usuario.correo == email
            )
        
        resultado = session.scalars(query)
        return resultado.one_or_none()
    