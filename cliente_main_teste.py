#from cliente_adm import *
from clientes.cliente_reg import *
from entidades.eleitores import *

dados = input("Digite nome, cpf e unidade: ")
dados = dados.split()
e = eleitor(dados[0], dados[1], dados[2])

sel = input("Registrar como eleitor: 1\nRegistrar como candidato, ou apoiar candidatura: 2\n")

