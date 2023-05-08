import csv

#salva os dados do eleitor no arquivo csv
def cadastra_eleitor(filename, nome, cpf, unidade):

    with open(filename, 'a') as arquivo_csv:
        escreve_csv = csv.writer(arquivo_csv)
        escreve_csv.writerow([nome, cpf, unidade, "0", "0"])

#verifica se os dados do eleitor está no arquivo csv
def busca_eleitor(filename, nome, cpf, unidade):
    
    with open(filename, "r") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        
        for linha in leitor_csv:
            if linha['validade'] == '1' and linha['unidade'] == unidade:
                if linha['nome'] == nome and linha['cpf'] == cpf:
                    return True
        return False
    
#busca os dados do eleitor no arquivo csv
def busca_dados(filename, nome, cpf, unidade):
    
    with open(filename, "r") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        
        for linha in leitor_csv:
            if linha['nome'] == nome and linha['cpf'] == cpf and linha['unidade'] == unidade:
                return True
        return False
    
#transforma o eleitor, uma vez que ele ja esteja nos arquivos, como um eleitor válido para eleição
def muda_estado_eleitor(filename, nome, cpf):

    with open(filename, "r+") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)

        cont = 35
        os = 0
        for linha in leitor_csv:
            if linha['nome'] == nome and linha['cpf'] == cpf:
                cont += (len(linha['nome'])+len(linha['cpf'])+len(linha['unidade'])+len(linha['validade'])+4)
                arquivo_csv.seek(cont+os, 0)
                arquivo_csv.write('1')
                return
            cont += (len(linha['nome'])+len(linha['cpf'])+len(linha['unidade'])+len(linha['validade'])+len(linha['candidato'])+5)
            os += 1

#regista um eleitor ja validado como candidato
def reg_candidato(filename, nome, cpf):

    with open(filename, "r+") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)

        cont = 35
        os = 0
        for linha in leitor_csv:
            if linha['nome'] == nome and linha['cpf'] == cpf:
                cont += (len(linha['nome'])+len(linha['cpf'])+len(linha['unidade'])+len(linha['validade'])+len(linha['candidato'])+5)
                arquivo_csv.seek(cont+os, 0)
                arquivo_csv.write('1')
                return
            cont += (len(linha['nome'])+len(linha['cpf'])+len(linha['unidade'])+len(linha['validade'])+len(linha['candidato'])+5)
            os += 1

#busca os dados de um candidato no arquivo csv
def busca_cand(filename, candList):

    with open(filename, 'r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)

        for linha in leitor_csv:
            if linha['candidato'] == "1":
                eleitor = [linha['nome'], linha['cpf'], linha['unidade'], linha['validade'], linha['candidato']]
                candList.append(eleitor)