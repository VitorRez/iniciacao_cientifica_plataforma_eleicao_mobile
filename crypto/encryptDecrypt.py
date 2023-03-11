from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class Encryptor:
    def __init__(self, rsa_key, aes_key):
        self.rsa_key = rsa_key
        self.aes_key = aes_key

    def encrypt_sym(self, msg):
        cipher = AES.new(self.aes_key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(msg.encode('utf-8'))
        return (nonce, ciphertext, tag)

    def decrypt_sym(self, nonce, ciphertext, tag, key):
        cipher = AES.new(key, AES.MODE_EAX, nonce)
        msg = cipher.decrypt(ciphertext)
        msg = bytes.decode(msg)
        return msg
    
    def encrypt(self, msg):
        key = RSA.import_key(self.rsa_key)
        cipher = PKCS1_OAEP.new(key)
        ciphertext = cipher.encrypt(str.encode(msg))
        return ciphertext
    
    def decrypt(self, ciphertext, rsa_key):
        key = RSA.import_key(rsa_key)
        cipher = PKCS1_OAEP.new(key)
        msg = cipher.decrypt(ciphertext)
        return bytes.decode(msg)

#text = "banana"
#chave_rsa = RSA.generate(1024)
#chave_aes = get_random_bytes(16)
#e = Encryptor(chave_rsa.public_key().export_key('PEM'), chave_aes)

#exemplo uso criptografia simetrica

#print("-----Criptografia simetrica-----")
#cipher_text = e.encrypt_sym(text)
#print(cipher_text[1])
#plain_text = e.decrypt_sym(cipher_text[0], cipher_text[1], cipher_text[2], e.aes_key)
#print(plain_text)

#exemplo uso criptografia assimetrica

#print("----Criptografia assimétrica----")
#cipher_text = e.encrypt(text)
#print(cipher_text)
#plain_text = e.decrypt(cipher_text, chave_rsa.export_key('PEM'))
#print(plain_text)