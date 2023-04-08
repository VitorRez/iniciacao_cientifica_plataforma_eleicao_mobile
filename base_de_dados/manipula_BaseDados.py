import csv
from Crypto.PublicKey import RSA
from crypto.encryptDecrypt import *
from crypto.PBKDF import *
from crypto.hashing import *

def cadastra_eleitor(filename, nome, cpf, unidade):

    with open(filename, 'a') as arquivo_csv:
        escreve_csv = csv.writer(arquivo_csv)
        escreve_csv.writerow([nome, cpf, unidade, "0", "0"])


def busca_eleitor(filename, nome, cpf, unidade):
    
    with open(filename, "r") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        
        for linha in leitor_csv:
            if linha['validade'] == '1' and linha['unidade'] == unidade:
                if linha['nome'] == nome and linha['cpf'] == cpf:
                    return True
        return False
    
def busca_dados(filename, nome, cpf, unidade):
    
    with open(filename, "r") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        
        for linha in leitor_csv:
            if linha['nome'] == nome and linha['cpf'] == cpf and linha['unidade'] == unidade:
                return True
        return False

def muda_estado_eleitor(filename, nome, cpf):

    with open(filename, "r+") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)

        cont = 35
        os = 0
        for linha in leitor_csv:
            if linha['nome'] == nome and linha['cpf'] == cpf:
                cont += (len(linha['nome'])+len(linha['cpf'])+len(linha['unidade'])+len(linha['validade'])+4)
                arquivo_csv.seek(cont+os, 0)
                arquivo_csv.write('1')
                return
            cont += (len(linha['nome'])+len(linha['cpf'])+len(linha['unidade'])+len(linha['validade'])+len(linha['candidato'])+5)
            os += 1

def reg_candidato(filename, nome, cpf):

    with open(filename, "r+") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)

        cont = 35
        os = 0
        for linha in leitor_csv:
            if linha['nome'] == nome and linha['cpf'] == cpf:
                cont += (len(linha['nome'])+len(linha['cpf'])+len(linha['unidade'])+len(linha['validade'])+len(linha['candidato'])+5)
                arquivo_csv.seek(cont+os, 0)
                arquivo_csv.write('1')
                return
            cont += (len(linha['nome'])+len(linha['cpf'])+len(linha['unidade'])+len(linha['validade'])+len(linha['candidato'])+5)
            os += 1

def busca_cand(filename, candList):

    with open(filename, 'r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)

        for linha in leitor_csv:
            if linha['candidato'] == "1":
                eleitor = [linha['nome'], linha['cpf'], linha['unidade'], linha['validade'], linha['candidato']]
                candList.append(eleitor)

def guarda_chave_priv(id, key, password):

    salt = get_salt(id)
    filename = f"{id}_priv.PEM"
    nonce, enc_key = encrypt_pbkdf(key, password, salt)
    p_hash = create_hash(password)
    store_hash(id, p_hash)
    with open(filename, "wb") as file:
        file.write(enc_key)
    filename = f"{id}_nonce.PEM"
    with open(filename, "wb") as file:
        file.write(nonce)
       
def busca_chave_pub(id, local):

    filename = f"{local}/certificado_{id}.pem"
    with open(filename, "r") as file:
        text = file.read()
        text = text.split("pub:\n            ")
        text = text[1].split("Signature")
        #print(text[0])
        pubkey = RSA.import_key(text[0])
        return pubkey
    
def busca_chave_priv(id, password):

    salt = get_salt(id)
    filename = f"{id}_priv.PEM"
    with open(filename, "rb") as file:
        enc_key = file.read()
    filename = f"{id}_nonce.PEM"
    with open(filename, "rb") as file:
        nonce = file.read()
    p_hash = get_hash(id)
    x = verify_hash(password, p_hash)
    if x:
        key = decrypt_pbkdf(nonce, enc_key, password, salt)
        return key
    else:
        return None
        
def store_salt(id, salt):

    filename = f"{id}_salt.txt"
    with open(filename, "wb") as file:
        file.write(salt)

def get_salt(id):

    filename = f"{id}_salt.txt"
    with open(filename, "rb") as file:
        salt = file.read()
        return salt
    
def store_hash(id, hash):

    filename = f"{id}_hash.txt"
    with open(filename, "wb") as file:
        file.write(hash)

def get_hash(id):

    filename = f"{id}_hash.txt"
    with open(filename, "rb") as file:
        hash = file.read()
        return hash
