import csv

lista = ["Márcio", "Luis", "João"]

idade = [15, 18, 12]

contador2 = 0

for contador in lista:

    data = [
        ['Nome', 'Idade'],
        [contador, idade[contador2]]
    ]

    contador2 += 1

    nome_arquivo = 'teste2.csv'

    with open(nome_arquivo, mode="w", newline='') as file:

        writer = csv.writer(file)

        writer.writerows(data)