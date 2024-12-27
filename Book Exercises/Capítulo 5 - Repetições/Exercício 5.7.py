contador = 1

while contador != 0:

    inicioTabuada = int(input("Digite o valor inicial da tabuada: "))

    fimTabuada = int(input("Digite o valor final da tabuada: "))

    for contador in range(inicioTabuada, fimTabuada + 1):

        print(contador * 2)

    print()

    contador = int(input("Digite 0 para interromper a execução: "))