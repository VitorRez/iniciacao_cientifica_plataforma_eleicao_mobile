from entidades.administrator import *
from entidades.registrar import *
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

def handle_client(conn, addr, reg, adm, tal, val):
    print(f"[NEW CONNECTION] {addr} connected.")

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
            if dados[0] == "registrar":
                admin(conn, addr, adm)
            if dados[0] == "administrator":
                regis(conn, addr, reg)
            if dados[0] == "validator":
                print()
            if dados[0] == "tallier":
                print()

    conn.close()

def admin(conn, addr, adm):

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
            if dados[0] == "candidatar":
                candidatar(conn, addr, adm)
            if dados[0] == "apoiar":
                apoiar(conn, addr, adm)

def candidatar(conn, addr, adm):
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            dados = msg.split()
            adm.candidato_a_candidato(dados[0], dados[1], dados[2])
            conn.send("Mensagem recebida".encode(FORMAT))

def apoiar(conn, addr, adm):
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            dados = msg
            print(f"[{addr}] {msg}")
            dados = msg.split()
            adm.registra_candidato(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5])
            conn.send("mensagem recebida".encode(FORMAT))

def regis(conn, addr, reg):
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            dados = msg.split()
            if dados[0] == "cadastrar":
                cadastrar(conn, addr, reg)
            if dados[0] == "autentificar":
                autentificar(conn, addr, reg)
            
def cadastrar(conn, addr, reg):
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            dados = msg.split()
            reg.cadastra_eleitor(dados[0], dados[1], dados[2])
            conn.send("mensagem recebida".encode(FORMAT))

def autentificar(conn, addr, reg):
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            dados = msg.split()
            reg.registra_eleitor(dados[0], dados[1], dados[2])
            conn.send("mensagem recebida".encode(FORMAT))

def start(reg, adm, tal, val):
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, reg, adm, tal, val))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")