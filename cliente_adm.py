import socket
from crypto.encryptDecrypt import *
from base_de_dados.manipula_BaseDados import *

HEADER = 1024
PORT = 5055
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

def send_to_adm(nome, cpf, unidade):
    chave_rsa = busca_chave_pub("adm")
    chave_aes = get_random_bytes(16)
    e = Encryptor(chave_rsa, chave_aes)
    info = nome + " " + cpf + " " + unidade
    cipher = e.protocolo_e(info)
    send(str(cipher[1]))
    send(str(cipher[0]))
    print(client.recv(2048).decode(FORMAT))

nome = input("[NOME]: ")
cpf = input("[CPF]: ")
unidade = input("[UNIDADE]: ")
send_to_adm(nome, cpf, unidade)
