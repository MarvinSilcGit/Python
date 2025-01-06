inicio_tabuada = int(input("Digite o valor inicial da tabuada: "))

for contador in range(1, 10 + 1):

    print("%d x %d = %d " % (inicio_tabuada, contador, inicio_tabuada * contador))