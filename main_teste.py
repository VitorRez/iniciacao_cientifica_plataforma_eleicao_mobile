import threading
import threading
import time
from certificados.autoridade_certificadora import *
from entidades.eleitores import *
from entidades.registrar import *
from entidades.administrator import *
from entidades.validator import *
from entidades.tallier import *
from entidades.autoridade import *
from servidores.server_registrar import *
from servidores.server_administrator import *
from crypto.encryptDecrypt import *

aut = autoridade()
reg = registrar()
adm = administrator()
val = validator()
tal = tallier()

autoridade_certificadora(aut, reg, adm, val, tal)

#start_reg(reg)
s_reg = server_reg(reg)
s_adm = server_adm(adm)
thread_reg = threading.Thread(target=s_reg.start_reg)
thread_adm = threading.Thread(target=s_adm.start_adm)
thread_reg.start()
thread_adm.start()
time.sleep(2)
event = threading.Event()
