cont = 1

while cont != 0:

    valor1 = int(input("digite um valor: "))

    valor2 = int(input("digite outro valor: "))

    valor3 = 1

    valor4 = 0

    valor5 = valor1

    while valor3 <= valor2-1:

        valor3 = valor3+1

        valor4 = valor4+valor1

        if valor4 < valor1:

            valor5 = 1

        elif valor4 >= valor1:

            valor4 = valor4+valor1

            print("%d+%d = %d" % (valor5, valor1, valor4))

            valor5 = valor4

            valor4 = valor4-valor1

    print()

    cont = int(input("Digite 0 para interromper a execução: "))
