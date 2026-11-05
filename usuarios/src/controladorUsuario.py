from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from servicioUsuario import *

router = APIRouter(prefix="/usuarios")

class crearUsuarioDTO(BaseModel):
    nombre: str
    apellido: str
    rut: str
    correo: EmailStr
    password: str

class iniciarSesionDTO(BaseModel):
    correo: EmailStr
    password: str


class cambiarPassDTO(BaseModel):
    correo: EmailStr
    new_pass: str

@router.post("/crear-usuario")
def crear_usuario_controller(user: crearUsuarioDTO):
    crear_usuario_service(user)
    return

@router.post("/inicar-sesion")
def iniciar_sesion_controller(credenciales: iniciarSesionDTO):
    iniciar_sesion_service(credenciales)

@router.get("/solicitar-cambio")
def solicitar_cambio_controller(email: EmailStr):
    solicitar_cambio_service(email)

@router.put("/cambiar-pass")
def cambiar_pass_controler(credenciales: cambiarPassDTO):
    cambiar_pass_service(credenciales)