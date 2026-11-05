def consultar_locales_service(radio, long, lat):
    resultado = consultar_locales_repo(radio, long, lat)
    return resultado