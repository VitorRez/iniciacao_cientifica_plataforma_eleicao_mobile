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
nonce_s, cipher_s, enc_aes_s = e.protocolo_e(msg_sign)
nonce, cipher, enc_aes = e.protocolo_e(msg)
plaintext_s = e.protocolo_d(nonce_s, cipher_s, enc_aes_s, chave_priv)
plaintext = e.protocolo_d(nonce, cipher, enc_aes, chave_priv)
s.verify(plaintext, plaintext_s, chave_pub)
#print(plaintext)
#plaintext_s = stringToByte(plaintext_s, cipher_s[1])
##print(plaintext_s)
#s.verify(plaintext, plaintext_s, chave_pub)

#msg_s = s.sign(msg)
#s.verify(msg, msg_s, chave_pub)
