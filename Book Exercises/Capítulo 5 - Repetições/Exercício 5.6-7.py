contador = 1

while contador != 0:

    inicioTabuada = int(input("Digite o valor inicial da tabuada: "))

    fimTabuada = int(input("Digite o valor final da tabuada: "))

    for contador in range(1, fimTabuada + 1):

        print("%d x %d = %d " % (inicioTabuada, contador, inicioTabuada * contador))

    print()

    contador = int(input("Digite 0 para interromper a execução: "))