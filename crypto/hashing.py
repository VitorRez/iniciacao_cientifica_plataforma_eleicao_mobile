from Crypto.Hash import SHA256

#cria uma hash de uma mensagem
def create_hash(text):
    t_hash = SHA256.new(bytes(text,'utf-8'))
    return t_hash.digest()

#verifica a hash de uma mensagem
def verify_hash(text, t_hash):
    t_hash1 = SHA256.new(bytes(text,'utf-8'))
    if t_hash == t_hash1.digest():
        return True
    return False