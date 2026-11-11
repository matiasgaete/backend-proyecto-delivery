from fastapi import FastAPI
from controladorLocales import router
import uvicorn


app = FastAPI()
app.include_router(router)