from bd import config
from fastapi import FastAPI
from controladorUsuario import router


app = FastAPI()
app.include_router(router)
