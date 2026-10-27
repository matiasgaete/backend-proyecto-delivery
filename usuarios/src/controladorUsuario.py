from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from servicioUsuario import crear_usuario_service

router = APIRouter(prefix="/usuarios")

class crearUsuarioDTO(BaseModel):
    nombre: str
    apellido: str
    rut: str
    correo: EmailStr
    password: str

@router.post("/crear-usuario")
def crear_usuario_controller(user: crearUsuarioDTO):
    crear_usuario_service(user)
    return
