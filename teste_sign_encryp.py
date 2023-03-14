from crypto.encryptDecrypt import *
from crypto.sign import *
from base_de_dados.manipula_BaseDados import *

chave_aes = get_random_bytes(16)
chave = RSA.generate(1024)
guarda_chave_pub("teste", chave)
guarda_chave_priv("teste", chave)

chave_pub = busca_chave_pub("teste")
chave_priv = chave.export_key('PEM')

msg = "banana"
s = signature(chave_priv)
e = Encryptor(chave_pub, chave_aes)
msg_sign = s.sign(msg)
msg_sign = byteToString(msg_sign)
cipher = e.protocolo_e(msg)

plaintext = e.protocolo_d(cipher[0], chave_priv, cipher[1])
#print(plaintext)
#plaintext = stringToByte(plaintext, cipher[1])
s.verify(plaintext)

