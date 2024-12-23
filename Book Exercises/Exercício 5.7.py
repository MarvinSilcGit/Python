cont = 1

while cont != 0:

    valor1 = int(input("digite o valor inicial da tabuada: "))

    valor2 = int(input("digite o valor final da tabuada: "))

    cont1 = 0

    while cont1 < valor2:

        cont1 = cont1+1

        valor3 = valor1*cont1

        print("%dx%d = %d" % (valor1, cont1, valor3))

        if cont1 == valor2:

            break

    print()

    cont = int(input("Digite 0 para interromper a execução: "))