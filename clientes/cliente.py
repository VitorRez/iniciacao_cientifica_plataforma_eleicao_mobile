import socket

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

def registrar(dados):
    msg = input("[DESEJA SE CADASTRAR OU AUTENTIFICAR REGISTRO?]: ")
    send(msg)
    if msg == 'cadastrar':
        send(dados)
        print(client.recv(2048).decode(FORMAT))
    if msg == 'autentificar':
        send(dados)
        print(client.recv(2048).decode(FORMAT))

def administrator(dados):
    msg = input("[DESEJA SE CANDIDATAR OU APOIAR CANDIDATURA?]: ")
    send(msg)
    if msg == 'candidatar':
        send(dados)
        print(client.recv(2048).decode(FORMAT))
    if msg == 'apoiar':
        new_msg = input("[DIGITE OS DADOS DO CANDIDATO]: ")
        send(dados + new_msg)
        print(client.recv(2048).decode(FORMAT))

def send_msg(nome, cpf, unidade):
    dados = nome + cpf + unidade
    msg = input()
    send(msg)
    if msg == "registrar":
        registrar(dados)
    if msg == "administrator":
        administrator(dados)