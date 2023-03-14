from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

class signature:
    def __init__(self, key):
        self.key = RSA.importKey(key)

    def sign(self, message):
        message_h = SHA256.new(str.encode(message))
        s = pkcs1_15.new(self.key).sign(message_h)
        return s
    
    def verify(self, message, signature, key):
        #key_rsa = RSA.import_key(key)
        message_h = SHA256.new(str.encode(message))
        try:
            pkcs1_15.new(key).verify(message_h, signature)
            print("A assinatura é válida")
        except(ValueError, TypeError):
            print("A assinatura não é válida")

