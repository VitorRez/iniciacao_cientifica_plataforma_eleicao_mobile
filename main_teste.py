from certificados.autoridade_certificadora import *
from entidades.eleitores import *
from entidades.registrar import *
from entidades.administrator import *
from entidades.validator import *
from entidades.tallier import *
from entidades.autoridade import *
from servidores.server_registrar import *
from servidores.server_administrator import *

aut = autoridade()
reg = registrar()
adm = administrator()
val = validator()
tal = tallier()

autoridade_certificadora(aut, reg, adm, val, tal)

start_reg(adm)

#nome = "vitor"
#cpf = "12373075628"
#unidade = "1"

#nome = [" "]
#while nome != "\n":
#    nome = input("Digite o nome: ")
#    cpf = input("Digite o cpf: ")
#    unidade = input("Digite a unidade: ")

#    reg.registra_eleitor("teste.csv", nome, cpf, unidade)