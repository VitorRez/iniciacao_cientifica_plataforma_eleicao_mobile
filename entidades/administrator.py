from Crypto.PublicKey import RSA
from Crypto import *
from certificados.autoridade_certificadora import *
from base_de_dados.manipula_BaseDados import *

class administrator():

    def __init__(self):
        self.chave = RSA.generate(1024)
        guarda_chave_pub('adm', self.chave)

    def candidatar(self, nome, cpf, unidade):
        x = busca_eleitor("base_de_dados/eleitores.csv", nome, cpf, unidade)
        if not x:
            return
        reg_candidato("base_de_dados/eleitores.csv", nome, cpf)
        
        
