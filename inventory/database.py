#Conexão ao Banco de Dados:
from sqlalchemy import create_engine #import create engine -> tendo seu uso na var engine
from sqlalchemy.ext.declarative import declarative_base # import da declarative_base -> tendo seu uso na var Base
from sqlalchemy.orm.session import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./store.db' #declaração do uso do banco

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})#Criação da engine com a variavel que tem o caminho do banco de dados local

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)#Criação da sessão local

Base = declarative_base()#Banco de Dados.

def get_db():
    db = SessionLocal()

    try:#tenta fazer a reprodução da var db
        yield db
    finally:
        db.close()