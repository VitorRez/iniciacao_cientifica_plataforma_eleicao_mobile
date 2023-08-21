from clientes.cliente_adm import *
from clientes.cliente_reg import *
from crypto.encryptDecrypt import *
from crypto.sign import *
from crypto.PBKDF import *
from crypto.blind import *
from ballotGenerator import *

nome = 'vitor'
cpf = "12373075628"
unidade = "1"
cargo = "presidente"
id = "13"
option = int(input('[QUAL SERVIDOR QUER ACESSAR:]\nREG = 0\nADM = 1\nPREENCHER CEDULA = 2: '))
if option == 0:
    send_to_reg(nome, cpf, unidade)
if option == 1:
    send_to_adm(nome, cpf, unidade, cargo, id)
if option == 2:
    candidatos = []
    num_cargos = busca_num_cargos(unidade)
    for i in range(int(num_cargos)):
        candidatos.append(int(input("- ")))
    ballot = generate_ballot(candidatos)
    chave_pub = busca_chave_pub(cpf, "clientes")
    r = get_random_bytes(16)
    blind_ballot = blind(ballot, chave_pub, r)
    clean_ballot = unblind(blind_ballot, chave_pub, r)
    print(blind_ballot)
    print()
    print(clean_ballot)
    print()
    print(ballot)