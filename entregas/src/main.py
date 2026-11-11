from fastapi import FastAPI
from controlerEntregas import router


app = FastAPI()
app.include_router(router)
