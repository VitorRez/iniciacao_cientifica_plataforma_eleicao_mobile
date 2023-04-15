from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

#classe com péssimo nome para encriptar e decriptar mensagens
class Encryptor:
    def __init__(self, rsa_key, aes_key):
        self.rsa_key = rsa_key
        self.aes_key = aes_key

    #realiza criptografia simétrica de mensagens a partir de uma chave aes
    def encrypt_sym(self, msg):
        cipher = AES.new(self.aes_key, AES.MODE_EAX)
        nonce = cipher.nonce
        if type(msg) == bytes:
            ciphertext, tag = cipher.encrypt_and_digest(msg)
        else:
            ciphertext, tag = cipher.encrypt_and_digest(msg.encode('utf-8'))
        return (nonce, ciphertext)

    #decripta uma mensagem encriptada por uma chave simétrica aes
    def decrypt_sym(self, nonce, ciphertext, key):
        cipher = AES.new(key, AES.MODE_EAX, nonce)
        msg = cipher.decrypt(ciphertext)
        if type(msg) != bytes:
            msg = bytes.decode(msg)
        return msg
    
    #encripta uma mensagem com uma chave RSA
    def encrypt(self, msg):
        key = self.rsa_key
        cipher = PKCS1_OAEP.new(key)
        ciphertext = cipher.encrypt(msg)
        return ciphertext
    
    #decrypta uma mensagem com uma chave RSA
    def decrypt(self, ciphertext, rsa_key):
        key = RSA.import_key(rsa_key)
        cipher = PKCS1_OAEP.new(key)
        msg = cipher.decrypt(ciphertext)
        return msg
    
    #protocolo para encriptar uma mensagem com uma chave simétrica e encriptar essa chave simétrica
    #com uma chave RSA
    def protocolo_e(self, msg):
        enc = self.encrypt_sym(msg)
        enc_rsa = self.encrypt(self.aes_key)
        return (enc[0], enc[1], enc_rsa)
    
    #protocolo para decriptar uma chave simétrica com uma chave RSA e decriptar uma mensagem com a 
    #chave simétrica decriptada
    def protocolo_d(self, nonce, cipher_text, aes_enc, rsa_key):
        aes_key = self.decrypt(aes_enc, rsa_key)
        msg = self.decrypt_sym(nonce, cipher_text, aes_key)
        return msg
    
#msg = 'banana'
#rsa_key = RSA.generate(1024)
#aes_key = get_random_bytes(16)
#e = Encryptor(RSA.import_key(rsa_key.public_key().export_key()), aes_key)
#nonce, cipher, enc_aes = e.protocolo_e(msg)
#print(cipher)
#plaintext = e.protocolo_d(nonce, cipher, enc_aes, rsa_key.export_key('PEM'))
#print(plaintext)