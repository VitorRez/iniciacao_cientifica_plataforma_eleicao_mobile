from Crypto.PublicKey import RSA
from Crypto import *
from certificados.autoridade_certificadora import *
from base_de_dados.manipula_BaseDados import *

class registrar():

    def __init__(self):
        self.chave = RSA.generate(2048)
    
    def registra_eleitor(self, filename, nome, cpf, unidade):
        #print(nome, cpf, unidade)
        x = busca_eleitor(filename, nome, cpf, unidade)
        if x:
            chave = RSA.generate(2048)
            muda_estado_eleitor(filename, nome, cpf)
            guarda_chave_pub("base_de_dados/chave_pub.csv", nome, cpf, unidade, chave.publickey().exportKey("PEM"))
            signature = request(0, nome, chave.publickey().exportKey("PEM"), self.chave)
            certificado("registrar", nome, chave.publickey().exportKey("PEM"), "BR", f"certificado{nome}.pem", signature)