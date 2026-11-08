from fastapi import FastAPI
from controladorReportes import router


app = FastAPI()
app.include_router(router)