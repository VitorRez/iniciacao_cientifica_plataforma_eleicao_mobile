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
        return (nonce, ciphertext)

    def decrypt_sym(self, nonce, ciphertext, key):
        cipher = AES.new(key, AES.MODE_EAX, nonce)
        msg = cipher.decrypt(ciphertext)
        msg = bytes.decode(msg)
        return msg
    
    def encrypt(self, msg):
        #key = RSA.import_key(self.rsa_key)
        key = self.rsa_key
        cipher = PKCS1_OAEP.new(key)
        ciphertext = cipher.encrypt(msg)
        return ciphertext
    
    def decrypt(self, ciphertext, rsa_key):
        key = RSA.import_key(rsa_key)
        #key = rsa_key
        cipher = PKCS1_OAEP.new(key)
        msg = cipher.decrypt(ciphertext)
        return msg
    
    def protocolo_e(self, msg):
        enc = self.encrypt_sym(msg)
        enc_rsa = self.encrypt(self.aes_key)
        list = [enc[0], enc[1], enc_rsa]
        size = len(enc[1])
        text = listToString(list)
        return (text, size)
    
    def protocolo_d(self, text, rsa_key, size):
        list = stringToList(text, size)
        aes_key = self.decrypt(list[2], rsa_key)
        msg = self.decrypt_sym(list[0], list[1], aes_key)
        return msg
    

def byteToString(byte):
    text = str(int.from_bytes(byte, 'big'))
    return text

def stringToByte(text, size):
    byte = int(text).to_bytes(size, 'big')
    return byte

def listToString(list):
    text = " ".join([byteToString(i) for i in list])
    return text

def stringToList(text, size):
    list = text.split()
    list[0] = stringToByte(list[0], 16)
    list[1] = stringToByte(list[1], size)
    list[2] = stringToByte(list[2], 128)
    return list
