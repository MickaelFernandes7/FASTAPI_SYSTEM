#Arquivo que contem os modelos do Swagger
from fastapi import APIRouter, Depends, status, HTTPException 
from .. import database, schemas, models
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy.orm import Session
from .. import oauth2

router = APIRouter()

#CAMPO ESTOQUE
@router.post("/estoque", tags=['estoque'], status_code=status.HTTP_201_CREATED)#Criamos um produto, e add no estoque com um BaseModel, que vem do arquivo schemas.py
def create_inventory(request: schemas.Estoque, db: Session = Depends(database.get_db), current_user:schemas.Usuario = Depends(oauth2.get_current_user)):#O request tem o modelo de base Blog do arq schemas, e o DB depende da função get_db que tem ligação com o Session_Local em ambos vem do arq. database.
    #Recebe o modelo estoque do arq. models através do param request, e exibe o nome, descricao, preco, e quantidade
    novo_estoque = models.Estoque(nome=request.nome, descricao=request.descricao, preco=request.preco, quantidade=request.quantidade)

    db.add(novo_estoque) #Adiciona a var novo_estoque, ao banco de dados 
    db.commit() #comita a ação anterior
    db.refresh(novo_estoque) #atualiza o banco de dados, com a var inserida
    return novo_estoque

@router.put('/estoque/{nome}', tags=['estoque'], status_code=status.HTTP_202_ACCEPTED)
def update_inventory(nome:str, request: schemas.Estoque, db: Session = Depends(database.get_db), current_user:schemas.Usuario = Depends(oauth2.get_current_user)):
    estoque = db.query(models.Estoque).filter(models.Estoque.nome == nome)
    if not estoque.first():
        #recebe o BaseModel Estoque do arq schemas, e realiza um filtro(filter) e faz uma comparação de com o Nome digitado for equivalente ao Nome armazenado no banco, e atualiza a 1° ocorrência
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Produto: {nome} descrito não encontrado.")
    estoque.update(request.dict())
    db.commit() #comita a ação anterior no banco de dados
    return 'updated'


@router.delete('/estoque/{nome}', tags=['estoque'] ,status_code=status.HTTP_204_NO_CONTENT)#DELETE é a função que deleta campos, do HTTP.
def delete_inventory(nome: str, db: Session = Depends(database.get_db), current_user:schemas.Usuario = Depends(oauth2.get_current_user)):#a var db depende da função get_db(que é a ligação ao banco de dados)
    #a var estoque, recebe o BaseModel Estoque do arq schemas, e realiza um filtro(filter) e faz uma comparação de o Nome digitado for equivalente ao Nome armazenado no banco, e exclui a 1° ocorrência
    estoque = db.query(models.Estoque).filter(models.Estoque.nome == nome).delete(synchronize_session=False)
    if not estoque:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Produto: {nome} descrito não encontrado')
    db.commit()#comita a ação anterior no banco de dados
    return 'deleted'


@router.get('/estoque/{nome}', tags=['estoque'], status_code=200, response_model=schemas.ExibeEstoque)
def show_inventory(nome:str, db: Session = Depends(database.get_db), current_user:schemas.Usuario = Depends(oauth2.get_current_user)):#a var db depende da função get_db(que é a ligação ao banco de dados)
    #a var blogs, recebe o BaseModel Estoque do arq schemas, e realiza um filtro(filter) e faz uma comparação de o Nome digitado for equivalente ao Nome armazenado no banco, retorna a 1°(first) ocorrência
    estoque = db.query(models.Estoque).filter(models.Estoque.nome == nome).first()

    if not estoque:#Se não achar o nome equivalente, retorna não encontrado 404. Se sim, segue a linha.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Produto: {nome} descrito não encontrado')
    return estoque

@router.get('/estoque', tags=['estoque'], response_model=List[schemas.ExibeEstoque])
def all_inventory(db: Session = Depends(database.get_db), current_user:schemas.Usuario = Depends(oauth2.get_current_user)):
    estoque = db.query(models.Estoque).all()#retorna todos os produtos cadastrados com o método .all()
    return estoque
#FIM CAMPO ESTOQUE

#CAMPO COMPRAS----------------------------------------------
#Insere as compras
@router.post('/compras', tags=['compras'], status_code=status.HTTP_201_CREATED)
def create_buy(request: schemas.Compras, db: Session = Depends(database.get_db), current_user:schemas.Usuario = Depends(oauth2.get_current_user)):
    nova_compra = models.Compras(nome=request.nome, preco=request.preco, quantidade=request.quantidade, mes_compra=request.mes_compra, valor_gasto=request.preco * request.quantidade)
    db.add(nova_compra)
    db.commit()
    db.refresh(nova_compra)
    return nova_compra

#Atualiza a compra pelo nome. Quando atualizar colocar o valor gasto manualmente
@router.put('/compras/{nome}', tags=['compras'], status_code=status.HTTP_202_ACCEPTED)
def update_buy(nome:str, request: schemas.Compras, current_user:schemas.Usuario = Depends(oauth2.get_current_user),db: Session = Depends(database.get_db)):
    compras = db.query(models.Compras).filter(models.Compras.nome == nome)
    if not compras.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Compra do Produto: {nome} descrito não encontrada.")
    compras.update(request.dict())
    db.commit()
    return 'updated'

#Deleta a Compra pelo nome
@router.delete('/compras/{nome}', tags=['compras'] ,status_code=status.HTTP_204_NO_CONTENT)#DELETE é a função que deleta campos, do HTTP.
def delete_buy(nome: str, current_user:schemas.Usuario = Depends(oauth2.get_current_user), db: Session = Depends(database.get_db)):
    compras = db.query(models.Compras).filter(models.Compras.nome == nome).delete(synchronize_session=False)
    if not compras:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Compra do produto {nome}, descrito não encontrada')
    db.commit()
    return 'deleted'

#Exibe todas as compras
@router.get('/compras', tags=['compras'], status_code=status.HTTP_200_OK, response_model=List[schemas.ExibeCompras])
def all_buy(db: Session = Depends(database.get_db), current_user:schemas.Usuario = Depends(oauth2.get_current_user)):
    compras = db.query(models.Compras).all()
    return compras

@router.get('/compras/{nome}', tags=['compras'], status_code=200, response_model=schemas.ExibeCompras)
def show_buy(nome:str, db: Session = Depends(database.get_db), current_user:schemas.Usuario = Depends(oauth2.get_current_user)):
    compra = db.query(models.Compras).filter(models.Compras.nome == nome).first()

    if not compra:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Compra do Produto: {nome} descrito não encontrado')
    return compra

#Exibe as compras de acordo com o mês
@router.get('/compras{mes}', tags=['compras'], status_code=status.HTTP_200_OK)
def show_month_buy(mes:str, db: Session = Depends(database.get_db), current_user:schemas.Usuario = Depends(oauth2.get_current_user)):
    mes = db.query(models.Compras).filter(models.Compras.mes_compra == mes).all()
    if not mes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Compras no mês: {mes} descrito não encontradas')
    return mes

#Campo Vendas ---------------------------------------------
@router.post('/vendas', tags=['vendas'], status_code=status.HTTP_201_CREATED)
def create_sell(request: schemas.Vendas, db: Session = Depends(database.get_db), current_user:schemas.Usuario = Depends(oauth2.get_current_user)):
    nova_venda = models.Vendas(nome=request.nome, preco=request.preco, quantidade=request.quantidade, mes_venda=request.mes_venda, valor_recebido=request.preco * request.quantidade)
    db.add(nova_venda)
    db.commit()
    db.refresh(nova_venda)
    return nova_venda

@router.put('/vendas/{nome}', tags=['vendas'], status_code=status.HTTP_202_ACCEPTED)
def update_sell(nome:str, request: schemas.Vendas, current_user:schemas.Usuario = Depends(oauth2.get_current_user),db: Session = Depends(database.get_db)):
    vendas = db.query(models.Vendas).filter(models.Vendas.nome == nome)
    if not vendas.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Venda do Produto: {nome} descrito não encontrada.")
    vendas.update(request.dict())
    db.commit()
    return 'updated'

@router.delete('/vendas/{nome}', tags=['vendas'] ,status_code=status.HTTP_204_NO_CONTENT)#DELETE é a função que deleta campos, do HTTP.
def delete_sell(nome: str, current_user:schemas.Usuario = Depends(oauth2.get_current_user), db: Session = Depends(database.get_db)):
    vendas = db.query(models.Vendas).filter(models.Vendas.nome == nome).delete(synchronize_session=False)
    if not vendas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Venda do produto: {nome} descrito não encontrada')
    db.commit()
    return 'deleted'


@router.get('/vendas', tags=['vendas'], status_code=status.HTTP_200_OK, response_model=List[schemas.ExibeVendas])
def all_sell(db: Session = Depends(database.get_db), current_user:schemas.Usuario = Depends(oauth2.get_current_user)):
    vendas = db.query(models.Vendas).all()
    return vendas

@router.get('/vendas/{nome}', tags=['vendas'], status_code=200, response_model=schemas.ExibeVendas)
def show_sell(nome:str, db: Session = Depends(database.get_db), current_user:schemas.Usuario = Depends(oauth2.get_current_user)):
    venda = db.query(models.Vendas).filter(models.Vendas.nome == nome).first()

    if not venda:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Venda do Produto com o Nome: {nome} descrito não encontrado')
    return venda

@router.get('/vendas{mes}', tags=['vendas'], status_code=status.HTTP_200_OK)
def show_month_sell(mes:str, db: Session = Depends(database.get_db), current_user:schemas.Usuario = Depends(oauth2.get_current_user)):
    mes = db.query(models.Vendas).filter(models.Vendas.mes_venda == mes).all()
    if not mes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Vendas no mês: {mes} descrito não encontradas')
    return mes