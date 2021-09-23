from sqlalchemy import Column, Integer, String#Import dos tipos de dados do SQLALCHEMY
from .database import Base #Import da var Base, do arq database. Base é o banco de dados

#Tabela Estoque
class Estoque(Base):#Um modelo com o parametro da var Base, do arq database
    __tablename__ = 'estoque'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(String)
    preco = Column(String)
    quantidade = Column(String)

#Tabela Compras
class Compras(Base):
    __tablename__ = 'compras'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    preco = Column(Integer)
    quantidade = Column(Integer)
    valor_gasto = Column(Integer)
    mes_compra = Column(String)

#Tabela Usuário
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer,primary_key=True,index=True)
    nome = Column(String)
    email = Column(String)
    password = Column(String)
