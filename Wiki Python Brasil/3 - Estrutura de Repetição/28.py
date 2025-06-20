contador = 1

custo_total = 0

custo_medio = 0

while contador != 0:

    quantidade_cds = int(input("Digite a quantidade de CDs na coleção: "))

    for contador2 in range(1, quantidade_cds + 1):

        valorCd = float(input(f"Digite o valor do {contador2}° CD: "))

        custo_total += valorCd

    custo_medio = custo_total / quantidade_cds

    print(f"O custo total foi {custo_total:.2f}, e o custo médio de cada CD é R$ {custo_medio:.2f}")

    print()

    contador = int(input("Digite 0 para interromper a execução: "))

    print()