contador = 1

custo_total = 0

custo_medio = 0

while contador != 0:

    quantidade_cds = int(input("Digite a quantidade de CDs na coleção: "))

    for contador2 in range(1, quantidade_cds + 1):

        print("Digite o valor do %d° CD" % contador2)

        valorCd = float(input(""))

        custo_total += valorCd

    custo_medio = custo_total / quantidade_cds

    print("O custo total foi %.2f, e o custo médio de cada CD é R$ %.2f" % (custo_total, custo_medio))

    print()

    contador = int(input("Digite 0 para interromper a execução: "))

    print()