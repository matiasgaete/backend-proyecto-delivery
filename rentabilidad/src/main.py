from fastapi import FastApi
from controladorRentabilidad import router

app = FastApi()
app.include_router(router)