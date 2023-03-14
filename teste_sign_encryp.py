from crypto.encryptDecrypt import *
from crypto.sign import *
from base_de_dados.manipula_BaseDados import *

chave_aes = get_random_bytes(16)
chave = RSA.generate(1024)
guarda_chave_pub("teste", chave)

chave_pub = busca_chave_pub("teste")
chave_priv = chave.export_key('PEM')

msg = "banana"
s = signature(chave_priv)
e = Encryptor(chave_pub, chave_aes)
msg_sign = s.sign(msg)
print(len(msg_sign))
msg_sign = byteToString(msg_sign)
cipher = e.protocolo_e(msg)
cipher_s = e.protocolo_e(msg_sign)

plaintext = e.protocolo_d(cipher[0], chave_priv, cipher[1])
plaintext_s = e.protocolo_d(cipher_s[0], chave_priv, cipher_s[1])
print(cipher_s[1])
#print(plaintext)
#plaintext_s = stringToByte(plaintext_s, cipher_s[1])
##print(plaintext_s)
#s.verify(plaintext, plaintext_s, chave_pub)

#msg_s = s.sign(msg)
#s.verify(msg, msg_s, chave_pub)
