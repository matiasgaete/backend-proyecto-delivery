from fastapi import FastAPI
from controlerEntregas import *


app = FastAPI()
app.include_router(router)