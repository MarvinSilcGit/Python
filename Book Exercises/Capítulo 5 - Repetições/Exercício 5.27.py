contador1 = 1

contador2 = 0

cont3 = 0

while contador1 != 0:

    valor1 = (input("Digite um número ou uma letra para saber se é palíndromo: "))

    valor2 = valor1

    while contador2 != len(valor1):

        valor3 = (valor1 [0 + contador2])

        contador2 += 1

        valor4 = (valor1 [0 - contador2])

        if valor3 == valor4:

            cont3 += 1

        elif valor3 != valor4:

            cont3 += 0

    if cont3 == contador2:

        print("%s é palíndromo" % valor1)

    elif cont3 != contador2:

        print("%s não é palíndromo" % valor1)

    print()

    cont3 = 0

    contador2 = 0

    contador1 = int(input("Digite 0 para interromper a execução: "))

    print()