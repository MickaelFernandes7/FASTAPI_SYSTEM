#Arquivo de modelos de resposta
from typing import Optional
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
#Fim Modelos de Estoque
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
#Fim Modelos de Compras
#Modelos Vendas
class Vendas(BaseModel):
    nome: str
    preco: int
    quantidade: int
    mes_venda: str
    valor_recebido: int

class ExibeVendas(BaseModel):
    nome:str
    preco: int
    quantidade: int
    mes_venda: str
    valor_recebido: int
    class Config():
        orm_mode = True
#Fim Modelo de Vendas
#Modelos de Usuários
class Usuario(BaseModel):
    nome:str
    email: str
    password: str
    

class ExibeUsuario(BaseModel):
    nome: str
    email: str
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str
#Fim modelo de Usuários

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    email: Optional[str] = None