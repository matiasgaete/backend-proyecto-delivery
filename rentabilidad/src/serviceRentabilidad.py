import httpx
import clienteEntregas as clE
import clienteLocales as clL


def calcular_rentabilidad_service(area):
    locales = clL.consultar_locales()
    entregas = clE.consultar_entregas()

    # como contrato se recibira un json, por tanto.json() devulve diccionario
    
    lista_locales = locales.json()
    id_locales = dic_locales["id"]
    for registro in lista_locales:
        registro["id"]

    respuesta_entregas = httpx.AsyncClent.get("url")
    dic_entregas = respuesta_entregas.json()
    id = dic_entregas["id"]
    rentabilidad_promedio = dic_entregas["promedio"]
    