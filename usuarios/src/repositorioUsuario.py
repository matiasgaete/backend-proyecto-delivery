from bd import config
from usuario import Usuario

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
    