import csv
from Crypto.PublicKey import RSA
from Crypto import *

#classe para armazenar todos os dados do .csv
class eleitor():

    def __init__(self, nome, cpf, unidade, validade = '0', candidato = '0', chave_pub = '0'):
        self.nome = nome
        self.cpf = cpf
        self.unidade = unidade
        self.validade = validade 
        self.candidato = candidato
        self.chave_pub = chave_pub


#classe que representa os eleitores que são candidatos
class candidatos():

    def __init__(self):
        self.cand_list = []
