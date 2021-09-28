#Arquivo para criação e consulta de Usuário
from fastapi import APIRouter, Depends, status, HTTPException
from .. import database, schemas, models, hashing
from sqlalchemy.orm import Session
from .. import oauth2

router = APIRouter()

#CAMPO USUÁRIO
@router.post('/user', response_model=schemas.ExibeUsuario, tags=['usuarios'])#Cria um usuário, com o request recebendo o modelo Usuario, do arq schemas, e fazendo a conexão ao banco de dados, com a var db
def create_user(request: schemas.Usuario, db: Session = Depends(database.get_db)):
    #puxa o modelo sql do usuario, e o liga com o request que recebe o modelo pydantic de usuario. E criptografa a senha, pegando o modelo do arq hashing
    novo_usuario = models.Usuario(nome=request.nome,email=request.email,password=hashing.Hash.bcrypt(request.password))  
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

#Atualiza a compra pelo nome. Quando atualizar colocar o valor gasto manualmente
@router.put('/user/{email}', tags=['usuarios'], status_code=status.HTTP_202_ACCEPTED)
def update_user(email:str, request: schemas.Usuario, db: Session = Depends(database.get_db), current_user:schemas.Usuario = Depends(oauth2.get_current_user)):
    user = db.query(models.Usuario).filter(models.Usuario.email == email)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuário com o e-mail {email} descrito não encontrada.")
    user.update(request.dict())
    db.commit()
    return 'updated'

#Deleta a Compra pelo nome
@router.delete('/user/{email}', tags=['usuarios'] ,status_code=status.HTTP_204_NO_CONTENT)#DELETE é a função que deleta campos, do HTTP.
def delete_user(email: str, db: Session = Depends(database.get_db), current_user:schemas.Usuario = Depends(oauth2.get_current_user)):
    vendas = db.query(models.Usuario).filter(models.Usuario.email == email).delete(synchronize_session=False)
    if not vendas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Usuário com o e-mail {email} descrito não encontrada')
    db.commit()
    return 'deleted'

@router.get('/user/{email}', tags=['usuarios'])#Exibe o usuario com base no e-mail
def get_user(email:str, db: Session = Depends(database.get_db), current_user:schemas.Usuario = Depends(oauth2.get_current_user)):
    user = db.query(models.Usuario).filter(models.Usuario.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Usuário com o email {email} descrito não encontrado')
    return user