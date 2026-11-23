from fastapi import APIRouter
from service import *
from pydantic import BaseModel, EmailStr


router = APIRouter(prefix="/auth")


class validarCredencialesDTO(BaseModel):
    correo: EmailStr
    password: str

@router.post("/validar-credenciales")
async def controller_validar_credenciales(credenciales: validarCredencialesDTO):
    return await service_validar_credenciales(credenciales)
    