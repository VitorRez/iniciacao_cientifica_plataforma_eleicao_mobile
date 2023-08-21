import socket
from crypto.encryptDecrypt import *
from crypto.PBKDF import *
from base_de_dados.DataBaseManagement import *
from base_de_dados.KeyManagement import *
from certificados.autoridade_certificadora import *
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from crypto.sign import *

HEADER = 1024
PORT = 5060
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send_to_val(cpf, unidade, ballot):
    client.connect(ADDR)
    password = input("password: ")
    chave_rsa = RSA.import_key(client.recv(2048))
    chave_rsa_priv = busca_chave_priv(f"clientes/{cpf}", password)
    if chave_rsa_priv != None:
        chave_rsa_pub = busca_chave_pub(cpf, "clientes").export_key()
        chave_aes = get_random_bytes(16)
        e = Encryptor(chave_rsa, chave_aes)
        s = signature
        info = cpf + " " + unidade + " " + ballot
        