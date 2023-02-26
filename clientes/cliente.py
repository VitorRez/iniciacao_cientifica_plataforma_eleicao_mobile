from cliente_adm import *
from cliente_reg import *
from entidades.eleitores import *

dados = input("Digite nome, cpf e unidade: ")
dados = dados.split()
e = eleitor(dados[0], dados[1], dados[2])

sel = input("Registrar como eleitor: 1\nRegistrar como candidato, ou apoiar candidatura: 2\n")
if sel == 1:
    send_to_reg(e.nome, e.cpf, e.unidade)
if sel == 2:
    send_to_adm(e.nome, e.cpf, e.unidade)