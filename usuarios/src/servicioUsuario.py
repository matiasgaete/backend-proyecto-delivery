from repositorioUsuario import crear_usuario_repo

def crear_usuario_service(user):
    try:
        crear_usuario_repo(user)
    except:
        print("error")
    return
