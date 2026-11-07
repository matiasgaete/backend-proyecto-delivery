import httpx


async def consultar_entregas(ids):
    async with httpx.AsyncClient() as client:
        respuesta_entregas = await client.get(
            "http://localhost:8002/entregas/entregas-id",
            params={
                "ids_locales": ids,
                "hora_peticion": "2026-11-30T13:30:00-03:00"
            }
        )
        return respuesta_entregas.json()