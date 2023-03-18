from Crypto.PublicKey import RSA
from Crypto.Signature import *
from Crypto.Hash import SHA256
from Crypto import *
import datetime


def request(version, subject_name, subjectPKInfo, issuerPriKey):
    request = "version: %d\nsubject_name: %s\nsubjectPKInfo: %s\n"%(version, subject_name, subjectPKInfo)
    request_b = str.encode(request)
    h = SHA256.new(request_b)
    #print(request)
    signature = pkcs1_15.new(issuerPriKey).sign(h)
    return signature

def certificado(issuer_name,sub_name, sub_pubkey, sub_country, cert_name, signature):
    cert = open(cert_name, "w")
    current_time = datetime.datetime.now()
    issuer_country = "BR"
    cert.write("Certificate:\n")
    cert.write("    Data:\n")
    cert.write("        Version:\n")
    cert.write("        Serial number:\n")
    cert.write("        Signature Algorithm: sha256WithRSAEncryption\n")
    cert.write("        Issuer: C=%s, O=%s\n"%(issuer_country, issuer_name))
    cert.write("        Validity:\n")
    cert.write("            Not Before: %d %d %d:%d:%d %d\n"%(current_time.month, current_time.day, current_time.hour, current_time.minute, current_time.second, current_time.year))
    cert.write("            Not After: %d %d %d:%d:%d %d\n"%(current_time.month, current_time.day, current_time.hour, current_time.minute, current_time.second, current_time.year+1))
    cert.write("        Subject: C=%s, ST=MG, O=%s\n"%(sub_country, sub_name))
    cert.write("        Subject Public Key Info:\n ")
    cert.write("            Public key algorithm: RSA\n    Public-key: (2048 bit)\n")
    cert.write("            Public-key: (1024 bit)\n")
    cert.write("            pub:\n")
    cert.write("            %s\n"%(sub_pubkey))
    cert.write("    Signature Algorithm: sha256WithRSAEncryption\n")
    cert.write("        %s\n"%(signature))
    cert.close()

def autoridade_certificadora(aut, reg, adm, val, tal):
    #aut.chave = RSA.generate(2048)
    #reg.chave = RSA.generate(2048)
    #adm.chave = RSA.generate(2048)
    #val.chave = RSA.generate(2048)
    #tal.chave = RSA.generate(2048)
    sign_aut_req = request(0, "autoridade_certificadora",aut.chave.public_key().export_key("PEM"), aut.chave)
    sign_reg_req = request(1, 'registrar', reg.chave.public_key().export_key("PEM"), reg.chave)
    sign_adm_req = request(2, 'adiminstrador', adm.chave.public_key().export_key("PEM"), adm.chave)
    sign_val_req = request(3, 'validator', val.chave.public_key().export_key("PEM"), val.chave)
    sign_tal_req = request(4, 'tallier', tal.chave.public_key().export_key("PEM"), tal.chave)
    certificado('autoridade_certificadora', 'autoridade_certificadora', aut.chave.public_key().export_key("PEM"), "BR", "certificados/certificado_autoridade_eleitoral.pem", sign_aut_req)
    certificado('autoridade_certificadora', 'registrar', reg.chave.publickey().exportKey("PEM"), "BR", "certificados/certificado_registrar.pem", sign_reg_req)
    certificado('autoridade_certificadora', 'adminstrador', adm.chave.publickey().exportKey("PEM"), "BR", "certificados/certificado_administrator.pem", sign_adm_req)
    certificado('autoridade_certificadora', 'validator', val.chave.publickey().exportKey("PEM"), "BR", "certificados/certificado_validator.pem", sign_val_req)
    certificado('autoridade_certificadora', 'tallier', tal.chave.publickey().exportKey("PEM"), "BR", "certificados/certificado_tallier.pem", sign_tal_req)
