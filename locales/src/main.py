from fastapi import FastAPI
from controladorLocales import router
import uvicorn


app = FastAPI()
app.include_router(router)
#uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)