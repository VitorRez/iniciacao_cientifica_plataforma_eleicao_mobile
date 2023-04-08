import socket
from crypto.encryptDecrypt import *
from crypto.PBKDF import *
from base_de_dados.manipula_BaseDados import *
from certificados.autoridade_certificadora import *
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

HEADER = 1024
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send(msg):
    message = msg
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def inscrever(info, e):
    nonce, cipher, enc_aes = e.protocolo_e(info)
    send(nonce)
    send(cipher)
    send(enc_aes)
    print(client.recv(2048).decode(FORMAT))

def gerar(info, e):
    password = input("Password: ")
    salt = get_random_bytes(16)
    dados = info.split()
    store_salt(f"clientes/{dados[1]}", salt)
    nonce, cipher, enc_aes = e.protocolo_e(info)
    key = RSA.generate(1024)
    guarda_chave_pub(f"clientes/{dados[1]}", key)
    guarda_chave_priv(f"clientes/{dados[1]}", key, password)
    sign = request(0, dados[0], key.public_key().export_key(), key)
    certificado("registrar", dados[0], key.public_key().export_key(), "BR", dados[1], "clientes", sign)
    send(nonce)
    send(cipher)
    send(enc_aes)
    send(key.public_key().export_key())
    print(client.recv(2048).decode(FORMAT))

def send_to_reg(nome, cpf, unidade):
    client.connect(ADDR)
    chave_rsa = RSA.import_key(client.recv(2048))
    chave_aes = get_random_bytes(16)
    e = Encryptor(chave_rsa, chave_aes)
    info = nome + " " + cpf + " " + unidade
    msg = input("[DESEJA SE INSCREVER OU GERAR PAR DE CHAVES?]: ")
    send(msg.encode(FORMAT))
    if msg == "inscrever":
        inscrever(info, e)
    if msg == "gerar":
        gerar(info, e)


