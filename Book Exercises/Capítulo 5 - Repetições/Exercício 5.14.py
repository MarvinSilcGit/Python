cont = 1

while cont != 0:

    valor1 = 1

    cont1 = 0

    cont2 = 0

    cont3 = 0

    while valor1 != 0:

        valor1 = int(input("digite um número: "))

        cont1 = cont1+valor1

        cont2 = cont2+1

        if valor1 == 0:

            cont2 = cont2-1

            if valor1 == 0:

                cont3 = cont1/cont2

                print("A iteração parou por ter digitado o número %d" % valor1)

                print("A média das somas dos números digitados é: %d . E o valor total da soma é: %d" % (cont3, cont1))

                break

    print()

    cont = int(input("Digite 0 para interromper a execução: "))

    print()
