from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class Encryptor:
    def __init__(self, key):
        self.key = key

    def encrypt_pub(self, message):
        cipher = PKCS1_OAEP.new(self.key.public_key())
        ciphertext = cipher.encrypt(message)
        return ciphertext
    
    def encrypt_priv(self, message):
        cipher = PKCS1_OAEP.new(self.key)
        ciphertext = cipher.encrypt(message)
        return ciphertext
    
    def decrypt(self, ciphertext, key):
        cipher = PKCS1_OAEP.new(key)
        message = cipher.decrypt(ciphertext)
        return bytes.decode(message)

chave = RSA.generate(1024)
txt = 'bananinha'
txt_b = str.encode(txt)
enc = Encryptor(chave)
txt_enc = enc.encrypt_pub(txt_b)
print(txt_enc)
txt_dec = enc.decrypt(txt_enc, chave)
print(txt_dec)