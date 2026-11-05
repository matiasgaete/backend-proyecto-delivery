def consultar_locales():
    respuesta_locales = httpx.AsyncClien.get("url")