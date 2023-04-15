import csv
from Crypto.PublicKey import RSA
from crypto.encryptDecrypt import *
from crypto.PBKDF import *
from crypto.hashing import *

#salva os dados do eleitor no arquivo csv
def cadastra_eleitor(filename, nome, cpf, unidade):

    with open(filename, 'a') as arquivo_csv:
        escreve_csv = csv.writer(arquivo_csv)
        escreve_csv.writerow([nome, cpf, unidade, "0", "0"])

#verifica se os dados do eleitor está no arquivo csv
def busca_eleitor(filename, nome, cpf, unidade):
    
    with open(filename, "r") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        
        for linha in leitor_csv:
            if linha['validade'] == '1' and linha['unidade'] == unidade:
                if linha['nome'] == nome and linha['cpf'] == cpf:
                    return True
        return False
    
#busca os dados do eleitor no arquivo csv
def busca_dados(filename, nome, cpf, unidade):
    
    with open(filename, "r") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        
        for linha in leitor_csv:
            if linha['nome'] == nome and linha['cpf'] == cpf and linha['unidade'] == unidade:
                return True
        return False

#transforma o eleitor, uma vez que ele ja esteja nos arquivos, como um eleitor válido para eleição
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

#regista um eleitor ja validado como candidato
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

#busca os dados de um candidato no arquivo csv
def busca_cand(filename, candList):

    with open(filename, 'r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)

        for linha in leitor_csv:
            if linha['candidato'] == "1":
                eleitor = [linha['nome'], linha['cpf'], linha['unidade'], linha['validade'], linha['candidato']]
                candList.append(eleitor)


#guarda a chave privada do eleitor, encriptada por uma senha 
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
       
#busca a chave publica de um eleitor ou entidade no seu respectivo certificado x509
def busca_chave_pub(id, local):

    filename = f"{local}/certificado_{id}.pem"
    with open(filename, "r") as file:
        text = file.read()
        text = text.split("pub:\n            ")
        text = text[1].split("Signature")
        #print(text[0])
        pubkey = RSA.import_key(text[0])
        return pubkey
    
#busca a chave privada encriptada de um eleitor ou entidade    
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
        
#guarda o sal usado para encriptar a chave privada
def store_salt(id, salt):

    filename = f"{id}_salt.txt"
    with open(filename, "wb") as file:
        file.write(salt)

#busca o sal usado para decriptar uma chave privada
def get_salt(id):

    filename = f"{id}_salt.txt"
    with open(filename, "rb") as file:
        salt = file.read()
        return salt
    
#guarda o hash da senha de um eleitor
def store_hash(id, hash):

    filename = f"{id}_hash.txt"
    with open(filename, "wb") as file:
        file.write(hash)

#busca o hash da senha de um eleitor
def get_hash(id):

    filename = f"{id}_hash.txt"
    with open(filename, "rb") as file:
        hash = file.read()
        return hash
