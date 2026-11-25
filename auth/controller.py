from fastapi import APIRouter
from service import *
from pydantic import BaseModel, EmailStr


router = APIRouter(prefix="/auth")


class validarCredencialesDTO(BaseModel):
    correo: EmailStr
    password: str
    device_id: str


class cerrarSesionDTO(BaseModel):
    refresh_token: str
    device_id: str


@router.post("/login")
async def login_controller(credenciales: validarCredencialesDTO):
    return await login_service(credenciales)


@router.get("/refresh")
async def controller_consutal_id(refresh_token, device_id):
    return await refrescar_token(device_id, refresh_token)


@router.post("/logout")
def logout_controller(credenciales: cerrarSesionDTO):
    return logout_service(credenciales.device_id, credenciales.refresh_token)
    