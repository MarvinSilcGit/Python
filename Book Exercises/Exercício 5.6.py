cont = 1

while cont != 0:

    valor1 = int(input("tabuada de: "))

    valor2 = 1

    while valor2 <= 10:

        valor3 = valor1*valor2

        print("%dx%d = %d" % (valor1, valor2, valor3))

        valor2 = valor2+1

    print()

    cont = int(input("Digite 0 para interromper a execução: "))
