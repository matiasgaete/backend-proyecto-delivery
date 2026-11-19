from fastapi import FastAPI
from controladorUsuario import router



app = FastAPI()
app.include_router(router)

with open("public_key.pem", "rb") as file:
    public_key = file.read()


