contador1 = 1

contador3 = 0

while contador1 != 0:

    valor1 = (input("Digite um número ou uma letra para saber se é palíndromo: "))

    for contador2 in range(0, len(valor1)):

        posicao1 = (valor1 [0 + contador2])

        contador2 += 1

        posicao2 = (valor1 [0 - contador2])

        if posicao1 == posicao2:

            contador3 += 1

    if contador3 == contador2:

        print("%s é palíndromo" % valor1)

    else:

        print("%s não é palíndromo" % valor1)

    print()

    contador3 = 0

    contador1 = int(input("Digite 0 para interromper a execução: "))

    print()