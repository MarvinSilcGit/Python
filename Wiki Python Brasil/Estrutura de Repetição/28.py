contador = 1

custoTotal = 0

custoMedio = 0

while contador != 0:

    quantidadeCds = int(input("Digite a quantidade de CDs na coleção: "))

    for contador2 in range(1, quantidadeCds + 1):

        print("Digite o valor do %d° CD" % contador2)

        valorCd = float(input(""))

        custoTotal += valorCd

    custoMedio = custoTotal / quantidadeCds

    print("O custo total foi %.2f, e o custo médio de cada CD é R$ %.2f" % (custoTotal, custoMedio))

    print()

    contador = int(input("Digite 0 para interromper a execução: "))

    print()