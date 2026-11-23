import jwt
from config import public_key
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


bearer_schema = HTTPBearer()

def validar_token(credenciales: HTTPAuthorizationCredentials = Depends(bearer_schema)):
    token = credenciales.credentials
    algorithms= ["ES256"]
    
    try:
        return jwt.decode(token, public_key, algorithms)
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="El token ha expirado"
            # agregar headers
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token invalido"
        )
    