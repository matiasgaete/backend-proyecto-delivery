from fastapi import FastAPI
from controller import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # O ["*"] en desarrollo
    allow_credentials=True,
    allow_methods=["*"],  # Esto permite OPTIONS, POST, GET, etc.
    allow_headers=["*"],  # Esto permite Content-Type: application/json
)