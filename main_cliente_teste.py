from clientes.cliente_adm import *
from clientes.cliente_reg import *
from crypto.encryptDecrypt import *
from crypto.sign import *
from crypto.PBKDF import *

nome = 'vitor'
cpf = "12373075628"
unidade = "1"
cargo = "presidente"
id = "13"
option = int(input('[QUAL SERVIDOR QUER ACESSAR:]\nREG = 0\nADM = 1: '))
if option == 0:
    send_to_reg(nome, cpf, unidade)
if option == 1:
    send_to_adm(nome, cpf, unidade, cargo, id)