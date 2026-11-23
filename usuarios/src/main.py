from fastapi import FastAPI
from controladorUsuario import router
from config import settings, public_key


app = FastAPI()
app.include_router(router)
