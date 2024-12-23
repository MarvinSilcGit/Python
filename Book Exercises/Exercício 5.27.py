cont = 1

cont2 = 0

cont3 = 0

while cont != 0:

    print("Um número ou uma letra para saber se é palíndromo.  É palíndromo quando, independente da ordem de leitura, é o mesmo. Ex: 545, 454, ovo, arara etc...")

    valor1 = (input("Digite um número ou uma letra para saber se é palíndromo: "))

    valor2 = valor1

    while cont2 != len(valor1):

        valor3 = (valor1[0+cont2])

        cont2 += 1

        valor4 = (valor1[0-cont2])

        if valor3 == valor4:

            cont3 += 1

        elif valor3 != valor4:

            cont3 += 0

    if cont3 == cont2:

        print("%s é palíndromo" % valor1)

    elif cont3 != cont2:

        print("%s não é palíndromo" % valor1)

    print()

    cont3 = 0

    cont2 = 0

    cont = int(input("Digite 0 para interromper a execução: "))

    print()
