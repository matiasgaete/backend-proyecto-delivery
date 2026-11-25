from bd import conf
from usuario import Usuario
from sqlalchemy import select, and_, update, func

def consultar_id_repo(id):
    with conf() as session:
        query = select(Usuario).where(
            and_(
                id == Usuario.id
                )
            )
        resultado = session.scalars(query)
        return resultado.one_or_none()

def crear_usuario_repo(user):
    with conf() as session:
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
    with conf() as session:
        query = select(Usuario).where(
            and_(
                credenciales.correo == Usuario.correo,
                credenciales.password == Usuario.pass_user
                )
            )
        resultado = session.scalars(query)
        return resultado.one_or_none()

def guardar_token_restablecimiento_repo(email, token_hash, expires_at):
    with conf() as session:
        result = session.execute(
            update(Usuario)
            .where(Usuario.correo == email)
            .values(
                reset_token_hash=token_hash,
                reset_token_expires_at=expires_at,
            )
        )
        session.commit()
        return result.rowcount > 0

def cambiar_pass_repo(email, token_hash, new_pass):
    with conf() as session:
        result = session.execute(
            update(Usuario)
            .where(
                Usuario.correo == email,
                Usuario.reset_token_hash == token_hash,
                Usuario.reset_token_expires_at > func.now(),
            )
            .values(
                pass_user=new_pass,
                reset_token_hash=None,
                reset_token_expires_at=None,
            )
        )
        session.commit()
        return result.rowcount > 0

def invalidar_token_restablecimiento_repo(token_hash):
    with conf() as session:
        session.execute(
            update(Usuario)
            .where(Usuario.reset_token_hash == token_hash)
            .values(reset_token_hash=None, reset_token_expires_at=None)
        )
        session.commit()

def solicitar_cambio_repo(email):
    with conf() as session:
        query = select(Usuario).where(
            Usuario.correo == email
            )
        
        resultado = session.scalars(query)
        return resultado.one_or_none()
    