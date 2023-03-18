from Crypto.Protocol.KDF import PBKDF2
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

def PBKDF(password, salt):
    keys = PBKDF2(password, salt, 16, count=1000000, hmac_hash_module=SHA256)
    return keys

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