from Crypto.PublicKey import RSA
from Crypto import *
from certificados.autoridade_certificadora import *
from base_de_dados.manipula_BaseDados import *

#classe que representa a entidade do validador
class validator():

    def __init__(self):
        self.chave = RSA.generate(2048)