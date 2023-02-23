from autoridade_certificadora import *
from eleitores import *
from registrar import *
from administrator import *
from validator import *
from tallier import *
from autoridade import *
from server_registrar import *

aut = autoridade()
reg = registrar()
adm = administrator()
val = validator()
tal = tallier()

autoridade_certificadora(aut, reg, adm, val, tal)

cand = candidatos()
cand.buscaCand("teste.csv")
for i in cand.cand_list:
    print(i.nome)

start(reg)

#nome = "vitor"
#cpf = "12373075628"
#unidade = "1"

#nome = [" "]
#while nome != "\n":
#    nome = input("Digite o nome: ")
#    cpf = input("Digite o cpf: ")
#    unidade = input("Digite a unidade: ")

#    reg.registra_eleitor("teste.csv", nome, cpf, unidade)