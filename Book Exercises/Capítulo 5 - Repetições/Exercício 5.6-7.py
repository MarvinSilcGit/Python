contador = 1

while contador != 0:

    inicio_tabuada = int(input("Digite o valor inicial da tabuada: "))

    fim_tabuada = int(input("Digite o valor final da tabuada: "))

    for contador in range(1, fim_tabuada + 1):

        print("%d x %d = %d " % (inicio_tabuada, contador, inicio_tabuada * contador))

    print()

    contador = int(input("Digite 0 para interromper a execução: "))