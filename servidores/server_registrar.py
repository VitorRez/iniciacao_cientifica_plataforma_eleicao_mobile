from entidades.registrar import *
from crypto.encryptDecrypt import *
import socket
import threading

HEADER = 1024
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr, reg):
    print(f"[NEW CONNECTION] {addr} connected.")
    chave_rsa = reg.chave.export_key('PEM')
    chave_aes = get_random_bytes(16)
    e_reg = Encryptor(chave_rsa, chave_aes)
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            dados = msg.split()
            if dados[0] == "inscrever":
                inscrever(conn, addr, reg, e_reg)
                connected = False
            if dados[0] == "gerar":
                gerar(conn, addr, reg, e_reg)
                connected = False
        
    conn.close()

def inscrever(conn, addr, reg, e_reg):
    print("[O CLIENTE IRA SE INSCREVER COMO ELEITOR]")
    size = get_size(conn, addr)
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            text = e_reg.protocolo_d(msg, e_reg.rsa_key, size)
            dados = text.split()
            reg.cadastra_eleitor(dados[0], dados[1], dados[2])
            conn.send("Eleitor inscrito!".encode(FORMAT))
            connected = False

def gerar(conn, addr, reg, e_reg):
    print("[O CLIENTE QUER GERAR UM PAR DE CHAVES]")
    size = get_size(conn, addr)
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            text = e_reg.protocolo_d(msg, e_reg.rsa_key, size)
            dados = text.split()
            reg.registra_eleitor(dados[0], dados[1], dados[2])
            conn.send("Par de chaves gerado!".encode(FORMAT))
            connected = False

def get_size(conn, addr):
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            return int(msg)

def start_reg(reg):
    server.listen()
    print(f"[LISTENING] Server is listerning on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, reg))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")