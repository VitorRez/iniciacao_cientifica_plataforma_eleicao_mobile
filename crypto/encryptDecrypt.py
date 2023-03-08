from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class Encryptor:
    def __init__(self, key):
        self.key = key

    def encrypt_sym(self, message):
        cipher = AES.new(self.aes_key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
        return (nonce, ciphertext, tag)

    def decrypt_sym(self, nonce, ciphertext, tag, key):
        cipher = AES.new(key, AES.MODE_EAX, nonce)
        message = cipher.decrypt(ciphertext)
        message = bytes.decode(message)
        return message

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
