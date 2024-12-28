contador1 = 1

while contador1 != 0:

    contador3 = 0

    valor1 = (input("Digite um número ou uma letra para saber se é palíndromo: "))

    if len(valor1) < 2:

        print("Tamanho insuficiente!")

        continue

    else:

        for contador2 in range(0, len(valor1)):

            if valor1 [0 + contador2] == valor1 [-1 - contador2]:

                contador3 += 1

        if contador3 == len(valor1):

            print("%s é palíndromo" % valor1)

        else:

            print("%s não é palíndromo" % valor1)

        print()

    contador1 = int(input("Digite 0 para interromper a execução: "))

    print()