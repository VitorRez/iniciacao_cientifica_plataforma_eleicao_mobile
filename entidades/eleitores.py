import csv
from Crypto.PublicKey import RSA
from Crypto import *

#classe para armazenar todos os dados do .csv
class eleitor():

    def __init__(self, nome, cpf, unidade, validade, candidato):
        self.nome = nome
        self.cpf = cpf
        self.unidade = unidade
        self.validade = validade 
        self.candidato = candidato


#classe que representa os eleitores que são candidatos
class candidatos():

    def __init__(self):
        self.cand_list = []

    #busca os candidatos na base de dado de eleitores
    def buscaCand(self, filename):

        with open(filename, 'r') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)

            for linha in leitor_csv:
                if linha['candidato'] == "1":
                    e = eleitor(linha['nome'], linha['cpf'], linha['unidade'], linha['validade'], linha['candidato'])
                    self.cand_list.append(e)