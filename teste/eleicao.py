import csv
from certificados.autoridade_certificadora import *
from base_de_dados.manipula_BaseDados import *
from Crypto.PublicKey import RSA
from Crypto import *

#classe para armazenar todos os dados do .csv
class eleitor():

    def __init__(self, nome, cpf, unidade, validade, candidato, data, horai, horaf):
        self.nome = nome
        self.cpf = cpf
        self.unidade = unidade
        self.validade = validade 
        self.candidato = candidato
        self.data = data
        self.horai = horai
        self.horaf = horaf

#classe que representa os eleitores que são candidatos
class candidatos():

    def __init__(self):
        self.cand_list = []

    #busca os candidatos na base de dado de eleitores
    def buscaCand(self, filename):
        aux = []
        busca_cand(filename, aux)
        for i in aux:
            e = eleitor(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
            self.cand_list.append(e)

#altera o arquivo .csv quando algum dado for alterado (chave publica, validade, etc)
#não está sendo usada
def writeDB(filename, eleitor_csv):
    
    with open(filename, "w+") as arquivo_csv:
        escreve_csv = csv.writer(arquivo_csv)
        escreve_csv.writerow(['nome','cpf','unidade','validade','candidato','data','horai','horaf','num_votos'])
        for linha in eleitor_csv:
            escreve_csv.writerow([linha['nome'], linha['cpf'], linha['unidade'], linha['validade'], linha['candidato'], linha['data'], linha['horai'], linha['horaf']])

#metodo pra guardar a chave publica do eleitor no arquivo especifico para isso
def guarda_chave_pub(filename, linha, chave):

    with open(filename, "a") as arquivo_csv:
        escreve_csv = csv.writer(arquivo_csv)
        escreve_csv.writerow([linha['nome'], linha['cpf'], linha['unidade'], chave])


#verifica se o individuo é um eleitor válido (não está votando uma segunda vez, vota naquela "unidade" e possui nome e cpf válido)
#se o eleitor for válido, é gerada um par de chaves do RSA, a chave publica é exportada para o arquivo que armazena as chaves publicas
#e a chave privada é enviada para o eleitor
#ao final altera o arquivo .csv
#leve sentimento que essa parte ta funcionando meio que na base da gambiarra, trecho sujeito a refinamento
def registrar_e(filename, nome, cpf, unidade):

    with open(filename, "r+") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)

        cont = 62
        offset = 0
        for linha in leitor_csv:
            if linha['validade'] == '1' and linha['unidade'] == unidade:
                if linha['nome'] == nome and linha['cpf'] == cpf:
                    chave = RSA.generate(2048)
                    cont += (len(linha['nome'])+len(linha['cpf'])+len(linha['unidade'])+len(linha['validade'])+4)
                    arquivo_csv.seek(cont+offset, 0)
                    arquivo_csv.write('0')
                    chave_pub = chave.publickey().exportKey("PEM")
                    guarda_chave_pub("chave_pub.csv", linha, chave_pub)
                    chave_priv = chave.export_key("PEM")
                    signature = request(0, nome,)
                    return chave_priv
            cont += (len(linha['nome'])+len(linha['cpf'])+len(linha['unidade'])+len(linha['validade'])+len(linha['candidato'])+len(linha['data'])+len(linha['horai'])+len(linha['horaf'])+len(linha['num_votos'])+9)
            offset += 1
        return None

#linhas para testar se ta funcionando
cand_list = []
#readDB("teste.csv", cand_list)
for i in cand_list:
    print(i.nome)
i = 1
while i == 1:
    nome = input()
    cpf = input()
    unidade = input()
    e = registrar_e("teste.csv", nome, cpf, unidade)
    if e != None:
        print(e)
    else:
        print("eleitor inválido")
    i = int(input())






            



