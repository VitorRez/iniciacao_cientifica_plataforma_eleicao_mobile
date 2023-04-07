from entidades.registrar import *
from crypto.sign import *
from crypto.encryptDecrypt import *
import socket
import threading

HEADER = 1024
PORT = 5055
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

def handle_client(conn, addr, adm):
    print(f"[NEW CONNECTION] {addr} connected.")
    chave_pub = adm.chave.public_key().export_key()
    conn.send(chave_pub)
    chave_rsa = adm.chave.export_key('PEM')
    chave_aes = get_random_bytes(16)
    e_adm = Encryptor(chave_rsa, chave_aes)
    s_adm = signature(chave_rsa)
    nonce = get_nonce(conn, addr)
    cipher = get_cipher(conn, addr)
    enc_aes = get_enc_aes(conn, addr)
    nonce_s = get_nonce(conn, addr)
    cipher_s = get_cipher(conn, addr)
    enc_aes_s = get_enc_aes(conn, addr)
    text = e_adm.protocolo_d(nonce, cipher, enc_aes, e_adm.rsa_key)
    text_s = e_adm.protocolo_d(nonce_s, cipher_s, enc_aes_s, e_adm.rsa_key)
    dados = text.split()
    chave_eleitor = RSA.import_key(get_key(conn, addr))
    s_adm.verify(text, text_s, chave_eleitor)
    try:
        adm.candidatar(dados[0].decode('utf-8'), dados[1].decode('utf-8'), dados[2].decode('utf-8'))
        conn.send("Candidatura aprovada".encode(FORMAT))
    except:
        conn.send("As chaves não correspondem".encode(FORMAT))
        conn.close()

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
        
def get_key(conn, addr):
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            key = conn.recv(msg_length)
            return key

class server_adm():
    def __init__(self, adm):
        self.adm = adm

    def start_adm(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(ADDR)
        server.listen()
        print(f"[LISTENING] Administrator server is listening on {SERVER}")
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr, self.adm))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

