import socket
from crypto.encryptDecrypt import *
from base_de_dados.manipula_BaseDados import *

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

def inscrever(info, e):
    cipher = e.protocolo_e(info)
    send(str(cipher[1]))
    send(str(cipher[0]))
    print(client.recv(2048).decode(FORMAT))

def gerar(info, e):
    cipher = e.protocolo_e(info)
    send(str(cipher[1]))
    send(str(cipher[0]))
    print(client.recv(2048).decode(FORMAT))

def send_to_reg(nome, cpf, unidade):
    chave_rsa = busca_chave_pub("reg")
    chave_aes = get_random_bytes(16)
    e = Encryptor(chave_rsa, chave_aes)
    info = nome + " " + cpf + " " + unidade
    msg = input("[DESEJA SE INSCREVER OU GERAR PAR DE CHAVES?]: ")
    send(msg)
    if msg == "inscrever":
        inscrever(info, e)
    if msg == "gerar":
        gerar(info, e)


nome = 'vitor'
cpf = "12373075628"
unidade = "1"
send_to_reg(nome, cpf, unidade)