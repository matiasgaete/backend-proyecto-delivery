import httpx


async def consultar_entregas(ids, hora_peticion, app, token):
    token = token["token"]
    async with httpx.AsyncClient() as client:
        respuesta_entregas = await client.get(
            "http://localhost:8002/entregas/entregas-id",
            params={
                "ids_locales": ids,
                "hora_peticion": hora_peticion.isoformat(),
                "app": app
            },
            headers={"Authorization": f"Bearer {token}"}
        )
        return respuesta_entregas.json()