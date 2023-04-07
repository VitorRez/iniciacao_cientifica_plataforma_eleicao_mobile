from Crypto.Protocol.KDF import PBKDF2
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from crypto.encryptDecrypt import *

def PBKDF(password, salt):
    keys = PBKDF2(password, salt, 16, count=1000000, hmac_hash_module=SHA256)
    return keys

def encrypt_pbkdf(key_rsa, password, salt):
    key_rsa = key_rsa.export_key('PEM')
    key_sym = PBKDF(password, salt)
    e = Encryptor(0, key_sym)
    enc_key = e.encrypt_sym(key_rsa)
    return enc_key

def decrypt_pbkdf(nonce, enc_key, password, salt):
    key_sym = PBKDF(password, salt)
    e = Encryptor(0, key_sym)
    key_rsa = e.decrypt_sym(nonce, enc_key, key_sym)
    return key_rsa

def verify_password(password, p_hash):
    p_hash1 = SHA256.new(bytes(password,'utf-8'))
    if p_hash == p_hash1:
        return True
    else:
        return False
    
#msg = 'banana'
#password = 'amobanana'
#salt = get_random_bytes(16)
#chave = PBKDF(password, salt)
#print(chave)
#e = Encryptor(0, chave)
#cipher = e.encrypt_sym(msg)
#new_key = PBKDF(password, salt)
#print(new_key)
#text = e.decrypt_sym(cipher[0], cipher[1], new_key)
#print(text.decode("utf-8"))