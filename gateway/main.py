from fastapi import FastAPI, Request, Response
import httpx

app = FastAPI(title="API Gateway")

# 1. Tabla de puertos internos de tu arquitectura
SERVICIOS = {
    "rentabilidad": "http://127.0.0.1:8001",
    "entregas":     "http://127.0.0.1:8002",
    "locales":      "http://127.0.0.1:8003",
    "reportes":     "http://127.0.0.1:8004",
    "usuarios":     "http://127.0.0.1:8005",
}

@app.api_route("/api/v1/{servicio}/{ruta_interna:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def reenviar_peticion(servicio: str, ruta_interna: str, request: Request, body:dict):
    if servicio not in SERVICIOS:
        return Response(content='{"error": "Servicio no encontrado"}', status_code=404)
    
    url_destino = f"{SERVICIOS[servicio]}/{servicio}/{ruta_interna}"

    async with httpx.AsyncClient() as client:
        respuesta = await client.request(
            method=request.method,
            url=url_destino,
            params=dict(request.query_params),
            content=await request.body(),
            headers=dict(request.headers)
        )

        return Response(
            content=respuesta.content,
            status_code=respuesta.status_code,
            headers=dict(respuesta.headers)
        )
    