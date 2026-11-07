from fastapi import FastAPI
from controlerEntregas import *
import uvicorn


app = FastAPI()
app.include_router(router)
uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)