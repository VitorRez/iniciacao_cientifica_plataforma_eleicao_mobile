from Crypto.PublicKey import RSA
from Crypto import *
from certificados.autoridade_certificadora import *
from base_de_dados.manipula_BaseDados import *

class registrar():

    def __init__(self):
        self.chave = RSA.generate(1024)
        guarda_chave_pub('reg', self.chave)
    
    def cadastra_eleitor(self, nome, cpf, unidade):
        cadastra_eleitor("base_de_dados/eleitores.csv", nome, cpf, unidade)

    def registra_eleitor(self, nome, cpf, unidade):
        #print(nome, cpf, unidade)
        filename = "base_de_dados/eleitores.csv"
        x = busca_dados(filename, nome, cpf, unidade)
        if x:
            chave = RSA.generate(1024)
            muda_estado_eleitor(filename, nome, cpf)
            guarda_chave_pub(cpf, chave)
            signature = request(0, nome, chave.publickey().exportKey("PEM"), self.chave)
            certificado("registrar", nome, chave.publickey().exportKey("PEM"), "BR", f"certificado{nome}.pem", signature)