from Crypto.PublicKey import RSA
from Crypto import *
from certificados.autoridade_certificadora import *
from base_de_dados.DataBaseManagement import *

#classe que representa a autoridade certificadora
class autoridade():

    def __init__(self):
        self.chave = RSA.generate(2048)