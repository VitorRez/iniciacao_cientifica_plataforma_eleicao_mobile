import socket
from crypto.encryptDecrypt import *
from base_de_dados.manipula_BaseDados import *
#from entidades.eleitores import *

HEADER = 1024
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def inscrever(info):
    send(info)
    print(client.recv(2048).decode(FORMAT))

def gerar(info):
    send(info)
    print(client.recv(2048).decode(FORMAT))

def send_to_reg(nome, cpf, unidade):
    chave = busca_chave_entidade("reg")
    e_sym = Encryptor(chave)
    info = nome + " " + cpf + " " + unidade
    cipher_info = e_sym.encrypt_sym(info)
    msg = input("[DESEJA SE INSCREVER OU GERAR PAR DE CHAVES?]: ")
    send(msg)
    if msg == "inscrever":
        inscrever(cipher_info)
    if msg == "gerar":
        gerar(cipher_info)


nome = input("[NOME]: ")
cpf = input("[CPF]: ")
unidade = input("[UNIDADE]: ")
send_to_reg(nome, cpf, unidade)
        
