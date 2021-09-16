from fastapi import FastAPI, Depends,status, Response, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()

    try:#tenta fazer a reprodução da var db
        yield db
    finally:
        db.close()



@app.post("/estoque")#Criamos um produto, e add no estoque com um modelo de base, que vem do arquivo schemas.py
def create(request: schemas.Estoque, db: Session = Depends(get_db)):#O request tem o modelo de base Blog do arq schemas, e o DB depende da função get_db que tem ligação com o Session_Local do arq database.
    
    #Recebe o modelo estoque do arq models através do param request, e exibe o title e o body
    novo_estoque = models.Estoque(nome=request.nome, descricao=request.descricao, preco=request.preco)
    
    db.add(novo_estoque) #Adiciona a var novo_estoque, ao banco de dados 
    db.commit() #comita a ação anterior
    db.refresh(novo_estoque) #atualiza o banco de dados, com a var inserida
    return novo_estoque

@app.put('/estoque/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Estoque, db: Session = Depends(get_db)):
    #recebe o BaseModel Estoque do arq schemas, e realiza um filtro(filter) e faz uma comparação de o ID digitado for equivalente ao ID armazenado no banco, e atualiza a 1° ocorrência
    db.query(models.Estoque).filter(models.Estoque.id == id).update(request.dict())
    db.commit() #comita a ação anterior no banco de dados
    return 'updated'


@app.delete('/estoque', status_code=204)#DELETE é a função que deleta campos, do HTTP.
def delete(id: int, db: Session = Depends(get_db)):#a var db depende da função get_db(que é a ligação ao banco de dados)
    #a var estoque, recebe o BaseModel Estoque do arq schemas, e realiza um filtro(filter) e faz uma comparação de o ID digitado for equivalente ao ID armazenado no banco, e exclui a 1° ocorrência
    estoque = db.query(models.Estoque).filter(models.Estoque.id == id).delete(synchronize_session=False)
    if not estoque:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Produto com o ID descrito não encoontrado')
    db.commit()#comita a ação anterior no banco de dados
    return 'done'

@app.get('/estoque')
def all(db: Session = Depends(get_db)):
    estoque = db.query(models.Estoque).all()
    return estoque

@app.get('/estoque/{id}', status_code=200)#GET é o protocolo de leitura HTTP
def show(id:int, db: Session = Depends(get_db)):#a var db depende da função get_db(que é a ligação ao banco de dados)
    #a var blogs, recebe o BaseModel Blog do arq schemas, e realiza um filtro(filter) e faz uma comparação de o ID digitado for equivalente ao ID armazenado no banco, retorna a 1°(first) ocorrência
    estoque = db.query(models.Estoque).filter(models.Estoque.id == id).first()

    if not estoque:#Se não achar o blog equivalente, retorna não encontrado 404. Se sim, segue a linha.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Estoque com o ID descrito não encoontrado')
    return estoque



#CAMPO VENDAS

#CAMPO COMPRAS
