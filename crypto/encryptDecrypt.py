from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class Encryptor:
    def __init__(self, key):
        self.key = key

    def encrypt_pub(self, message):
        cipher = PKCS1_OAEP.new(self.key.public_key())
        ciphertext = cipher.encrypt(str.encode(message))
        return ciphertext
    
    def encrypt_priv(self, message):
        cipher = PKCS1_OAEP.new(self.key)
        ciphertext = cipher.encrypt(str.encode(message))
        return ciphertext
    
    def decrypt(self, ciphertext, key):
        cipher = PKCS1_OAEP.new(key)
        message = cipher.decrypt(ciphertext)
        return bytes.decode(message)
