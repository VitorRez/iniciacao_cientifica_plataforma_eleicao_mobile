from Crypto.Random import get_random_bytes
from bitstring import BitArray
from base_de_dados.DataBaseManagement import *
from random import randint

def generate_padding(k):
    position = randint(1, k - 1)
    i = 1
    pre = get_random_bytes(1)
    while pre == b'\x00':
        pre = get_random_bytes(1)
    pos = get_random_bytes(1)
    while pos == b'\x00':
        pos = get_random_bytes(1)
    while i < position:
        b = get_random_bytes(1)
        while b == b'\x00':
            b = get_random_bytes(1)
        pre = b + pre
        i += 1
    while i < k - 2:
        b = get_random_bytes(1)
        while b == b'\x00':
            b = get_random_bytes(1)
        pos = b + pos
        i += 1

    return pre, pos

def remove_padding(ballot):
    cont = 1
    clean_ballot = []
    i = 0
    while i < len(ballot):
        if ballot[i] == 0 and i+1 < len(ballot):
            if cont <= 2:
                clean_ballot.append(ballot[i+1])
                cont += 1
            else:
                clean_ballot.append(int.from_bytes(ballot[i+1:i+3], byteorder='big'))
                i += 1
        i += 1
    return clean_ballot[0:-1]

def get_num_bytes(candidatos):
    if len(candidatos) <= 2:
        num_bytes = 4
    else:
        num_bytes = 4 + 3*(len(candidatos) - 2)
    return num_bytes

def generate_ballot(candidatos):
    cont = 0
    size = 1
    num_bytes = get_num_bytes(candidatos)
    k = 256 - num_bytes
    pre, pos = generate_padding(k)
    pre = pre + b'\x00'
    for i in candidatos:
        pre = pre + i.to_bytes(size, "big") + b'\x00'
        if cont >= 1 and size < 2:
            size += 1
        cont += 1
    #print(len(pre))
    candidatos_bytes = pre + pos
    return candidatos_bytes

#teste
#candidatos = [1, 11, 111, 1111]
#ballot = generate_ballot(candidatos)
#clean_ballot = remove_padding(ballot)
#print(ballot)
#print(clean_ballot)