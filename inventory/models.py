#Arquivo que contem os modelos do banco de dados
from sqlalchemy import Column, Integer, String, Float#Import dos tipos de dados do SQLALCHEMY
from .database import Base #Import da var Base, do arq database. Base é o banco de dados

#Tabela Estoque
class Estoque(Base):#Um modelo com o parametro da var Base, do arq database
    __tablename__ = 'estoque'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(String)
    preco = Column(Float)
    quantidade = Column(Integer)

#Tabela Compras
class Compras(Base):
    __tablename__ = 'compras'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    preco = Column(Float)
    quantidade = Column(Integer)
    valor_gasto = Column(Float)
    mes_compra = Column(String)

#Tabela Vendas
class Vendas(Base):
    __tablename__ = 'vendas'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    preco = Column(Float)
    quantidade = Column(Integer)
    valor_recebido = Column(Float)
    mes_venda = Column(String)

#Tabela Usuário
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer,primary_key=True,index=True)
    nome = Column(String)
    email = Column(String)
    password = Column(String)
