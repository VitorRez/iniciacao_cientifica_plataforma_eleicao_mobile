from Crypto.PublicKey import RSA
from Crypto.Signature import *
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from Crypto.Cipher import *
from Crypto import *

message = "bananinha"
message_b = str.encode(message)
message_h = SHA256.new(message_b)
chave_teste = RSA.generate(1024)
message_e = message_h.encrypt(chave_teste)
#message_e = pkcs1_15.new(chave_teste).sign(message_h)
#message1 = "batatinha"
#message_b1 = str.encode(message1)
#message_h1 = SHA256.new(message_b1)
#message_e1 = pkcs1_15.new(chave_teste).sign(message_h1)
#pkcs1_15.new(chave_teste).verify(message_h, message_e)