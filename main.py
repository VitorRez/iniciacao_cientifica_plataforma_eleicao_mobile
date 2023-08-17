import threading
from certificados.autoridade_certificadora import *
from base_de_dados.election import *
from entidades.eleitores import *
from entidades.registrar import *
from entidades.administrator import *
from entidades.validator import *
from entidades.tallier import *
from entidades.autoridade import *
from servidores.server_registrar import *
from servidores.server_administrator import *
from crypto.encryptDecrypt import *

def main():
    aut = autoridade()
    reg = registrar()
    adm = administrator()
    val = validator()
    tal = tallier()

    autoridade_certificadora(aut, reg, adm, val, tal)

    estado = 0
    while estado == 0:
        create_election()
        estado = 1
    while estado == 1:
        s_reg = server_reg(reg)
        s_adm = server_adm(adm)
        thread_reg = threading.Thread(target=s_reg.start_reg)
        thread_adm = threading.Thread(target=s_adm.start_adm)
        thread_reg.start()
        thread_adm.start()
        estado = int(input("Digite 0 para encerrar pre-eleição " ))
    while estado == 0:
        thread_reg._stop.set()
        print(estado)
        
    
main()
