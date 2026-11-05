from fastapi import FastAPI
from controladorLocales import router


app = FastAPI()
app.include_router(router)