from entidades.registrar import *
from crypto.encryptDecrypt import *
import socket
import threading

HEADER = 2048
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

def handle_client(conn, addr, reg):
    print(f"[NEW CONNECTION] {addr} connected.")
    chave_pub = reg.chave.public_key().export_key()
    conn.send(chave_pub)
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
    nonce = get_nonce(conn, addr)
    cipher = get_cipher(conn, addr)
    enc_aes = get_enc_aes(conn, addr)
    text = e_reg.protocolo_d(nonce, cipher, enc_aes, e_reg.rsa_key)
    dados = text.split()
    reg.cadastra_eleitor(dados[0].decode('utf-8'), dados[1].decode('utf-8'), dados[2].decode('utf-8'))
    conn.send("Eleitor cadastrado".encode(FORMAT))


def gerar(conn, addr, reg, e_reg):
    print("[O CLIENTE IRA SE INSCREVER COMO ELEITOR]")
    nonce = get_nonce(conn, addr)
    cipher = get_cipher(conn, addr)
    enc_aes = get_enc_aes(conn, addr)
    text = e_reg.protocolo_d(nonce, cipher, enc_aes, e_reg.rsa_key)
    dados = text.split()
    chave = RSA.import_key(get_key(conn, addr))
    reg.registra_eleitor(dados[0].decode('utf-8'), dados[1].decode('utf-8'), dados[2].decode('utf-8'))
    conn.send("Par de chaves gerado".encode(FORMAT))

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

class server_reg():
    def __init__(self, reg):
        self.reg = reg

    def start_reg(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(ADDR)
        server.listen()
        print(f"[LISTENING] Registrar server is listerning on {SERVER}")
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr, self.reg))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")