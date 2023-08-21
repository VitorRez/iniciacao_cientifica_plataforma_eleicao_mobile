from entidades.validator import *
from crypto.sign import *
from crypto.encryptDecrypt import *
import socket
import threading

HEADER = 1024
PORT = 5060
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

def handle_client(conn, addr, val):
    print(f"[NEW CONNECTION] {addr} connected.")
    chave_pub = val.chave.public_key().export_key()
    conn.send(chave_pub)
    chave_rsa = val.chave.export_key('PEM')
    chave_aes = get_random_bytes(16)
    v_reg = Encryptor(chave_rsa, chave_aes)
    connected = True
    while connected:
        msg_lenght = conn.recv(HEADER).decode(FORMAT)
        if msg_lenght:
            msg_lenght = int(msg_lenght)
            msg = conn.recv(msg_lenght).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            dados = msg.split()
            print(dados)

def server_val():
    def __init__(self, val):
        self.val = val

    def start_val(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(ADDR)
        server.listen()
        print(f"[LISTENING] Validator server is listening on {SERVER}")
        try:
            while True:
                conn, addr = server.accept()
                thread = threading.Thread(target=handle_client, args=(conn, addr, self.val))
                thread.start()
                print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        finally:
            print("[SERVER CLOSED]")