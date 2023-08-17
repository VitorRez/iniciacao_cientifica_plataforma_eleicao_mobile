import csv

def busca_arquivo_eleitor(unidade):
    with open("base_de_dados/eleicao.csv", "r") as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        for linha in leitor_csv:
            if linha['nome'] == unidade:
                filename = linha['eleitores']
                return filename
        return False
            
def busca_arquivo_candidato(unidade):
    with open("base_de_dados/eleicao.csv", "r") as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        for linha in leitor_csv:
            if linha['nome'] == unidade:
                filename = linha['candidatos']
                return filename
        return False
            
def busca_arquivo_cargos(unidade):
    with open("base_de_dados/eleicao.csv", "r") as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        for linha in leitor_csv:
            if linha['nome'] == unidade:
                filename = linha['cargos']
                return filename
        return False
    
def busca_num_cargos(unidade):
    with open("base_de_dados/eleicao.csv", "r") as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        for linha in leitor_csv:
            if linha['nome'] == unidade:
                num_cargos = linha['num_cargos']
                return num_cargos
        return False

#salva os dados do eleitor no arquivo csv
def cadastra_eleitor(nome, cpf, unidade):

    filename = busca_arquivo_eleitor(unidade)

    if filename == False:
        return

    with open(filename, 'a') as arquivo_csv:
        escreve_csv = csv.writer(arquivo_csv)
        escreve_csv.writerow([nome, cpf, unidade, "0", "0"])

#verifica se os dados do eleitor está no arquivo csv
def busca_eleitor(nome, cpf, unidade):
    
    filename = busca_arquivo_eleitor(unidade)

    if filename == False:
        return

    with open(filename, "r") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        
        for linha in leitor_csv:
            if linha['validade'] == '1' and linha['unidade'] == unidade:
                if linha['nome'] == nome and linha['cpf'] == cpf:
                    return True
        return False
    
#busca os dados do eleitor no arquivo csv
def busca_dados(nome, cpf, unidade):
    
    filename = busca_arquivo_eleitor(unidade)
    if filename == False:
        return

    with open(filename, "r") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        
        for linha in leitor_csv:
            if linha['nome'] == nome and linha['cpf'] == cpf and linha['unidade'] == unidade:
                return True
        return False
    
#transforma o eleitor, uma vez que ele ja esteja nos arquivos, como um eleitor válido para eleição
def muda_estado_eleitor(nome, cpf, unidade):

    filename = busca_arquivo_eleitor(unidade)
    if filename == False:
        return

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

def lista_cargos(unidade, cargo):

    filename = busca_arquivo_cargos(unidade)

    if filename == False:
        return 
    
    cargos = []
    with open(filename, "r") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)

        for linha in leitor_csv:
            cargos.append(linha['nome'])

    return cargos


#regista um eleitor ja validado como candidato
def reg_candidato(nome, cpf, unidade, cargo, id):

    filename_e = busca_arquivo_eleitor(unidade)
    filename_c = busca_arquivo_candidato(unidade)

    if filename_e == False or filename_c == False:
        return

    with open(filename_e, "r+") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)

        cont = 35
        os = 0
        for linha in leitor_csv:
            if linha['nome'] == nome and linha['cpf'] == cpf:
                cont += (len(linha['nome'])+len(linha['cpf'])+len(linha['unidade'])+len(linha['validade'])+len(linha['candidato'])+5)
                arquivo_csv.seek(cont+os, 0)
                arquivo_csv.write('1')
                with open(filename_c, "a") as arquivo_csv:
                    escreve_csv = csv.writer(arquivo_csv)
                    escreve_csv.writerow([nome, cpf, unidade, cargo, id])
                return
            cont += (len(linha['nome'])+len(linha['cpf'])+len(linha['unidade'])+len(linha['validade'])+len(linha['candidato'])+5)
            os += 1

