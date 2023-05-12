from Crypto.PublicKey import RSA
from Crypto import *
from certificados.autoridade_certificadora import *
from base_de_dados.DataBaseManagement import *

#classe que representa a entidade do registrador
class registrar():

    def __init__(self):
        self.chave = RSA.generate(1024)
    
    def cadastra_eleitor(self, nome, cpf, unidade):
        cadastra_eleitor(nome, cpf, unidade)

    def registra_eleitor(self, nome, cpf, unidade):
        #print(nome, cpf, unidade)
        x = busca_dados(nome, cpf, unidade)
        if x:
            #chave = RSA.generate(1024)
            muda_estado_eleitor(nome, cpf, unidade)
            #guarda_chave_pub(cpf, chave)
            #guarda_chave_priv(cpf, chave)
            #signature = request(0, nome, chave.publickey().exportKey("PEM"), self.chave)
            #certificado("registrar", nome, chave.publickey().exportKey("PEM"), "BR", f"certificado{nome}.pem", signature)