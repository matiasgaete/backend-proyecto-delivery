from fastapi import FastAPI
from controlerEntregas import *
import uvicorn


app = FastAPI()
app.include_router(router)