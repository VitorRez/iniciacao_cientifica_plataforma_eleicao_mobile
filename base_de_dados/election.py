import csv

def create_election():

    cont = 1
    with open("base_de_dados/eleicao.csv", 'w') as arquivo_csv:
        escreve_csv = csv.writer(arquivo_csv)
        escreve_csv.writerow(["nome", "eleitores","candidatos","num_cargos"])
        num_cargos = int(input("Quantos cargos? Digite 0 para encerrar: "))
        while num_cargos != 0:
            cargos = []
            num_digitos = 2
            for i in range(num_cargos):
                txt = input("Digite o nome do cargo: ")
                cargos.append(txt)
            escreve_csv.writerow([str(cont), f"base_de_dados/eleitores/eleitores_{cont}.csv", f"base_de_dados/candidatos/candidatos_{cont}.csv", num_cargos, f"base_de_dados/cargos/cargos_{cont}.csv"])
            with open(f"base_de_dados/eleitores/eleitores_{cont}.csv", "w") as arquivo_eleitor:
                escreve_e = csv.writer(arquivo_eleitor)
                escreve_e.writerow(["nome","cpf","unidade","validade","candidato"])
            with open(f"base_de_dados/candidatos/candidatos_{cont}.csv", "w") as arquivo_candidato:
                escreve_c = csv.writer(arquivo_candidato)
                escreve_c.writerow(["nome","cpf","unidade","cargo","id"])
            with open(f"base_de_dados/cargos/cargos_{cont}.csv", "w") as arquivo_cargos:
                escreve_ca = csv.writer(arquivo_cargos)
                escreve_ca.writerow(["nome","num_digtos"])
                for i in cargos:
                    escreve_ca.writerow([i, str(num_digitos)])
                    num_digitos += 1
            cont += 1
            num_cargos = int(input("Quantos cargos? Digite 0 para encerrar: "))

#create_election()

        
     

