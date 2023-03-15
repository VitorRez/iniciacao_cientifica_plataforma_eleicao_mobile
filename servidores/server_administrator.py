from entidades.registrar import *
from crypto.encryptDecrypt import *
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
    chave_rsa = adm.chave.export_key('PEM')
    chave_aes = get_random_bytes(16)
    e_adm = Encryptor(chave_rsa, chave_aes)
    nonce = get_nonce(conn, addr)
    cipher = get_cipher(conn, addr)
    enc_aes = get_enc_aes(conn, addr)
    text = e_adm.protocolo_d(nonce, cipher, enc_aes, e_adm.rsa_key)
    dados = text.split()
    adm.candidatar(dados[0], dados[1], dados[2])
    conn.send("Candidatura aprovada".encode(FORMAT))

    conn.close()

def get_nonce(conn, addr):
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            nonce = conn.recv(msg_length)
            return nonce
        
def get_cipher(conn, addr):
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            cipher = conn.recv(msg_length)
            return cipher
            

def get_enc_aes(conn, addr):
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            enc_aes = conn.recv(msg_length)
            return enc_aes

def start_adm(adm):
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, adm))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

