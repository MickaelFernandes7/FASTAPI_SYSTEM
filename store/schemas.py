from pydantic import BaseModel

#Modelos Estoque
class Estoque(BaseModel):
    nome: str
    descricao: str
    preco: int
    quantidade: int

class ExibeEstoque(BaseModel):#Exibe os dados em um dict
    nome:str
    descricao:str
    preco: int
    quantidade: int
    
    class Config():
        orm_mode = True


#Modelos Usuários
class Usuario(BaseModel):
    nome:str
    email: str
    password: str
    

class ExibeUsuario(BaseModel):
    nome: str
    email: str
    class Config():
        orm_mode = True


#Modelos Compras
class Compras(BaseModel):
    nome: str
    preco: int
    quantidade: int
    mes_compra: str
    valor_gasto: int

class ExibeCompras(BaseModel):
    nome:str
    preco: int
    quantidade: int
    mes_compra: str
    valor_gasto: int
    class Config():
        orm_mode = True