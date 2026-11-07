from bd import config
from usuario import Usuario
from sqlalchemy import select, and_, update

def crear_usuario_repo(user):
    with config() as session:
        # Usuario(nombre_atributo_clase1="valor", nombre_atributo_clase2="valor")
        nuevo_usuario = Usuario(nombre=user.nombre,
                                apellido=user.apellido,
                                rut=user.rut,
                                correo=user.correo,
                                pass_user=user.password)
        
        session.add(nuevo_usuario)
        session.commit()
    return

def inicar_sesion_repo(credenciales):
    with config() as session:
        query = select(Usuario).where(
            and_(
                credenciales.correo == Usuario.correo,
                credenciales.password == Usuario.pass_user
                )
            )
        resultado = session.scalars(query)
        return resultado.one_or_none()

def cambiar_pass_repo(credenciales):
    with config() as session:
        query = (
            update(Usuario)
            .where(credenciales.correo == Usuario.correo)
            .values(pass_user=credenciales.new_pass)
            )

        result = session.execute(query)
        session.commit()

        if result.rowcount == 0:
            return False  # O lanzar una excepción personalizada (ej. UsuarioNoEncontradoError)
            
        return True

def solicitar_cambio_repo(email):
    with config() as session:
        query = select(Usuario).where(
            Usuario.correo == email
            )
        
        resultado = session.scalars(query)
        return resultado.one_or_none()
    