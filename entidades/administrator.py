from Crypto.PublicKey import RSA
from Crypto import *
from certificados.autoridade_certificadora import *
from base_de_dados.manipula_BaseDados import *

#classe que representa a entidade administrador
class administrator():

    def __init__(self):
        self.chave = RSA.generate(1024)

    #metodo para um eleitor se candidatar
    def candidatar(self, nome, cpf, unidade):
        x = busca_eleitor("base_de_dados/eleitores.csv", nome, cpf, unidade)
        if not x:
            return
        reg_candidato("base_de_dados/eleitores.csv", nome, cpf)
        
        
