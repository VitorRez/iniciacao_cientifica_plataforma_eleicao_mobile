from Crypto.PublicKey import RSA
from Crypto import *
from certificados.autoridade_certificadora import *
from base_de_dados.manipula_BaseDados import *

class administrator():

    def __init__(self):
        self.chave = RSA.generate(2048)

    def candidato_a_candidato(self, nome, cpf, unidade):
        x = busca_eleitor("base_de_dados/eleitores.csv", nome, cpf, unidade)
        if not x:
            return
        possiveis_candidatos(nome, cpf)

    def registra_candidato(self, enome, ecpf, eunidade, cnome, ccpf, cunidade):
        e = busca_eleitor("base_de_dados/eleitores.csv", enome, ecpf, eunidade)
        c = busca_eleitor("base_de_dados/eleitores.csv", cnome, ccpf, cunidade)
        if not e or not c:
            return
        incrementa_candidato(cnome, ccpf)
        
        
