import csv

data = [
    ['Sexo', 'População'],
    ['Homens', 93406990],
    ['Mulheres', 97348809],
    ['Total', 93406990 + 97348809]
]

nome_arquivo = 'teste.csv'

with open(nome_arquivo, mode="w", newline='') as file:

    writer = csv.writer(file)

    writer.writerows(data)