#Arquivo de uso e validação do Token
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from . import token

ouath2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(data:str = Depends(ouath2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Dados digitados não validados",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token.verify_token(data, credentials_exception)