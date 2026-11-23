import httpx


async def consultar_locales(lat, long, radio, token):
    token = token["token"]
    async with httpx.AsyncClient() as client:
        respuesta_locales = await client.get(
            "http://localhost:8003/locales/consultar-locales",
            params={
                "radio": radio,
                "long": long,
                "lat": lat
            },
            headers={"Authorization": f"Bearer {token}"}
        )
        return respuesta_locales.json()