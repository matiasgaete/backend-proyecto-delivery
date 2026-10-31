from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from servicioUsuario import crear_usuario_service, consultar_usuario_service, cambiar_pass_service

router = APIRouter(prefix="/usuarios")

class crearUsuarioDTO(BaseModel):
    nombre: str
    apellido: str
    rut: str
    correo: EmailStr
    password: str

class cambiarPassDTO(BaseModel):
    correo: EmailStr
    new_pass: str

@router.post("/crear-usuario")
def crear_usuario_controller(user: crearUsuarioDTO):
    crear_usuario_service(user)
    return

@router.get("/consultar-usuario")
def consultar_usuario_controller(correo: EmailStr, rut: str):
    consultar_usuario_service(correo, rut)

@router.put("/cambiar-pass")
def cambiar_pass_controler(credenciales: cambiarPassDTO):
    cambiar_pass_service(credenciales)