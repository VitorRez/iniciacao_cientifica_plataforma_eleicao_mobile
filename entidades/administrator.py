from Crypto.PublicKey import RSA
from Crypto import *
from certificados.autoridade_certificadora import *
from base_de_dados.DataBaseManagement import *

#classe que representa a entidade administrador
class administrator():

    def __init__(self):
        self.chave = RSA.generate(1024)

    #metodo para um eleitor se candidatar
    def candidatar(self, nome, cpf, unidade, cargo, id):
        x = busca_eleitor(nome, cpf, unidade)
        if not x:
            return
        reg_candidato(nome, cpf, unidade, cargo, id)
        
        
