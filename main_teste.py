import threading
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

start_reg(reg)