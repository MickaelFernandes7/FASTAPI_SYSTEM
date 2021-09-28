#Arquivo de Login de Usuário
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from .. import database, models, token
from ..hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter()

@router.post('/login', tags=['Authentication'])
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    #Puxa no banco de dados o modelo Usuario, e o email do modelo usuario ira receber o username(email) do request, e retorna o 1°
    user = db.query(models.Usuario).filter(models.Usuario.email == request.username).first()
    if not user:#Compara se o e-mail digitado tem um usuario cadastrado
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"E-mail Incorreto")
    #Compara a senha
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Senha Incorreta")
    #Gera um código jwt e o retorna, e recebe os dados do arq token
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}