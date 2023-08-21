from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
import numpy

def blind(message, key, r):
    blind_ballot = (int.from_bytes(message, "big")^(int.from_bytes(r, "big")^key.e))%key.n
    return blind_ballot.to_bytes(256, "big")

def unblind(blind_m, key, r):
    x = -1
    clean_ballot = (blind_m*int.from_bytes(r, "big")^(int.from_bytes(x, "big")))%key.n
    return clean_ballot.to_butes(256, "big")

