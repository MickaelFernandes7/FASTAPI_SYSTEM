from fastapi import FastAPI, Depends,status, HTTPException
from . import schemas, models, hashing
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List


app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()

    try:#tenta fazer a reprodução da var db
        yield db
    finally:
        db.close()


#CAMPO ESTOQUE
@app.post("/estoque", tags=['estoque'], status_code=status.HTTP_201_CREATED)#Criamos um produto, e add no estoque com um modelo de base, que vem do arquivo schemas.py
def create_inventory(request: schemas.Estoque, db: Session = Depends(get_db)):#O request tem o modelo de base Blog do arq schemas, e o DB depende da função get_db que tem ligação com o Session_Local do arq database.
    #Recebe o modelo estoque do arq models através do param request, e exibe o title e o body
    novo_estoque = models.Estoque(nome=request.nome, descricao=request.descricao, preco=request.preco, quantidade=request.quantidade)
    
    db.add(novo_estoque) #Adiciona a var novo_estoque, ao banco de dados 
    db.commit() #comita a ação anterior
    db.refresh(novo_estoque) #atualiza o banco de dados, com a var inserida
    return novo_estoque

@app.put('/estoque/{nome}', tags=['estoque'], status_code=status.HTTP_202_ACCEPTED)
def update_inventory(nome:str, request: schemas.Estoque, db: Session = Depends(get_db)):
    estoque = db.query(models.Estoque).filter(models.Estoque.nome == nome)
    if not estoque.first():
        #recebe o BaseModel Estoque do arq schemas, e realiza um filtro(filter) e faz uma comparação de com o Nome digitado for equivalente ao Nome armazenado no banco, e atualiza a 1° ocorrência
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Produto com o Nome descrito não encontrado.")
    estoque.update(request.dict())
    db.commit() #comita a ação anterior no banco de dados
    return 'updated'


@app.delete('/estoque/{nome}', tags=['estoque'] ,status_code=status.HTTP_204_NO_CONTENT)#DELETE é a função que deleta campos, do HTTP.
def delete_inventory(nome: str, db: Session = Depends(get_db)):#a var db depende da função get_db(que é a ligação ao banco de dados)
    #a var estoque, recebe o BaseModel Estoque do arq schemas, e realiza um filtro(filter) e faz uma comparação de o Nome digitado for equivalente ao Nome armazenado no banco, e exclui a 1° ocorrência
    estoque = db.query(models.Estoque).filter(models.Estoque.nome == nome).delete(synchronize_session=False)
    if not estoque:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Produto com o Nome descrito não encontrado')
    db.commit()#comita a ação anterior no banco de dados
    return 'deleted'

@app.get('/estoque', tags=['estoque'], response_model=List[schemas.ExibeEstoque])
def all_inventory(db: Session = Depends(get_db)):
    estoque = db.query(models.Estoque).all()
    return estoque

@app.get('/estoque/{nome}', tags=['estoque'], status_code=200, response_model=schemas.ExibeEstoque)#GET é o protocolo de leitura HTTP
def show_inventory(nome:str, db: Session = Depends(get_db)):#a var db depende da função get_db(que é a ligação ao banco de dados)
    #a var blogs, recebe o BaseModel Estoque do arq schemas, e realiza um filtro(filter) e faz uma comparação de o Nome digitado for equivalente ao Nome armazenado no banco, retorna a 1°(first) ocorrência
    estoque = db.query(models.Estoque).filter(models.Estoque.nome == nome).first()

    if not estoque:#Se não achar o nome equivalente, retorna não encontrado 404. Se sim, segue a linha.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Produto com o Nome {nome} do produto descrito não encontrado')
    return estoque

#CAMPO COMPRAS
#Exibe todas as compras
@app.get('/compras', tags=['compras'], status_code=status.HTTP_200_OK, response_model=List[schemas.ExibeCompras])
def all_buy(db: Session = Depends(get_db)):
    compras = db.query(models.Compras).all()
    return compras

#Insere as compras
@app.post('/compras', tags=['compras'], status_code=status.HTTP_201_CREATED)
def create_buy(request: schemas.Compras, db: Session = Depends(get_db)):
    nova_compra = models.Compras(nome=request.nome, preco=request.preco, quantidade=request.quantidade, mes_compra=request.mes_compra, valor_gasto=request.preco * request.quantidade)
    db.add(nova_compra)#Adiciona a var nova_compra, ao banco de dados
    db.commit() #comita a ação anterior
    db.refresh(nova_compra)#atualiza o banco de dados
    return nova_compra

@app.get('/compras/{nome}', tags=['compras'], status_code=200, response_model=schemas.ExibeCompras)#GET é o protocolo de leitura HTTP
def show_buy(nome:str, db: Session = Depends(get_db)):#a var db depende da função get_db(que é a ligação ao banco de dados)
    #a var blogs, recebe o BaseModel Estoque do arq schemas, e realiza um filtro(filter) e faz uma comparação de o Nome digitado for equivalente ao Nome armazenado no banco, retorna a 1°(first) ocorrência
    compra = db.query(models.Compras).filter(models.Compras.nome == nome).first()

    if not compra:#Se não achar o nome equivalente, retorna não encontrado 404. Se sim, segue a linha.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Compra do Produto com o Nome {nome} descrito não encontrado')
    return compra

#Exibe as compras de acordo com o mês
@app.get('/compras{mes}', tags=['compras'], status_code=status.HTTP_200_OK)
def show_month(mes:str, db: Session = Depends(get_db)):
    mes = db.query(models.Compras).filter(models.Compras.mes_compra == mes).all()
    if not mes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Compras no mes descrito não encontradas')
    return mes

#CAMPO USUÁRIO
@app.post('/user', response_model=schemas.ExibeUsuario, tags=['usuarios'])#Cria um usuário, com o request recebendo o modelo Usuario, do arq schemas, e fazendo a conexão ao banco de dados, com a var db
def create_user(request: schemas.Usuario, db: Session = Depends(get_db)):
    #puxa o modelo sql do usuario, e o liga com o request que recebe o modelo pydantic de usuario. E criptografa a senha, pegando o modelo do arq hashing
    novo_usuario = models.Usuario(nome=request.nome,email=request.email,password=hashing.Hash.bcrypt(request.password))  
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

@app.get('/user/{nome}', tags=['usuarios'])#Exibe o usuario com base no nome
def get_user(nome:str, db: Session = Depends(get_db)):
    user = db.query(models.Usuario).filter(models.Usuario.nome == nome).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Usuário com o Nome {nome} descrito não encontrado')
    return user


#CAMPO VENDAS


