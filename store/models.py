from sqlalchemy import Column, Integer, String #Import dos tipos de dados do SQLALCHEMY
from .database import Base #Import da var Base, do arq database

class Estoque(Base):#Um modelo com o parametro da var Base, do arq database
    __tablename__ = 'estoque'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(String)
    preco = Column(String)