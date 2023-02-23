import csv

def busca_eleitor(filename, nome, cpf, unidade):
    
    with open(filename, "r") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        
        for linha in leitor_csv:
            if linha['validade'] == '1' and linha['unidade'] == unidade:
                if linha['nome'] == nome and linha['cpf'] == cpf:
                    return True
        return False

def muda_estado_eleitor(filename, nome, cpf):

    with open(filename, "r+") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)

        cont = 35
        os = 0
        for linha in leitor_csv:
            if linha['nome'] == nome and linha['cpf'] == cpf:
                cont += (len(linha['nome'])+len(linha['cpf'])+len(linha['unidade'])+len(linha['validade'])+4)
                arquivo_csv.seek(cont+os, 0)
                arquivo_csv.write('0')
                return
            cont += (len(linha['nome'])+len(linha['cpf'])+len(linha['unidade'])+len(linha['validade'])+len(linha['candidato'])+9)
            os += 1

def possiveis_candidatos(nome, cpf):

    with open("possiveis_candidatos", "a") as arquivo_csv:
        escreve_csv = csv.writer(arquivo_csv)
        escreve_csv.writerow([nome, cpf, "0"])

def incrementa_candidato(nome, cpf):

    with open("possiveis_candidatos", "r+") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        
        cont = 14
        os = 0
        for linha in leitor_csv:
            if linha['nome'] == nome and linha['cpf'] == cpf:
                cont += (len(linha['nome']) + len(linha['cpf']) + len(linha['valor']) + 3)
                x = int(linha['valor'])
                x += 1
                if x == 3:
                    reg_candidato("teste.csv", nome, cpf)
                arquivo_csv.seek(cont+os, 0)
                arquivo_csv.write(x)
                return
            cont += (len(linha['nome']) + len(linha['cpf']) + len(linha['valor']) + 3)
            os += 1

def reg_candidato(filename, nome, cpf):

    with open(filename, "r+") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)

        cont = 62
        os = 0
        for linha in leitor_csv:
            if linha['nome'] == nome and linha['cpf'] == cpf:
                cont += (len(linha['nome']+linha['cpf']+linha['unidade']+linha['validade']+linha['candidato'])+5)
                arquivo_csv.seek(cont+os, 0)
                arquivo_csv.write('0')
                return
            cont += (len(linha['nome'])+len(linha['cpf'])+len(linha['unidade'])+len(linha['validade'])+len(linha['candidato'])+5)
            os += 1

def busca_cand(filename, candList):

    with open(filename, 'r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)

        for linha in leitor_csv:
            if linha['candidato'] == "1":
                eleitor = [linha['nome'], linha['cpf'], linha['unidade'], linha['validade'], linha['candidato']]
                candList.append(eleitor)

def guarda_chave_pub(filename, nome, cpf, unidade, chave):

    with open(filename, "a") as arquivo_csv:
        escreve_csv = csv.writer(arquivo_csv)
        escreve_csv.writerow([nome, cpf, unidade, chave])

def busca_chave_pub(filename, nome, cpf, unidade):

    with open(filename, "r") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)

        for linha in leitor_csv:
            if linha['nome'] == nome and linha['cpf'] == cpf and linha['unidade'] == unidade:
                chave = linha['chave']
                return chave