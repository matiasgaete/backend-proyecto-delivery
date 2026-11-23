import httpx


async def consultar_credenciales(credenciales):
    async with httpx.AsyncClient() as client:
        respuesta = await client.post(
            "http://127.0.0.1:8005/usuarios/iniciar-sesion",
            json={
                "correo": credenciales.correo,
                "password": credenciales.password
            }
        )
        return respuesta
