from fastapi import FastAPI
from controladorRentabilidad import router

app = FastAPI()
app.include_router(router)