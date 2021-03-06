#Arquivo para criptografar a senha
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated="auto")

class Hash():
    def bcrypt(password: str):
#Criptografia de senha:  recebe a var pwd_cxt, passa por um rash com o valor de request password como paraemtro
        return pwd_cxt.hash(password)
    #Compara a senha
    def verify(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password, hashed_password)