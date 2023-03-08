from entidades.administrator import *
import socket
import threading

HEADER = 1024
PORT = 5055
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr, adm):
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
            adm.candidatar(dados[0], dados[1], dados[2])
            conn.send("Candidadura concluída".encode(FORMAT))

    conn.close()

def start_adm(adm):
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, adm))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

