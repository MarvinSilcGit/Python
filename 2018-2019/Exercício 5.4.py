cont = 1

while cont != 0:

    valor1 = int(input("Digite o valor inicial: "))

    valor2 = int(input("Digite o valor final: "))

    if valor1 != 1:

        print("Número incorreto")

        break

    elif valor1 == 1:

        cont1 = 0

        while valor1 < valor2:

            print(valor1)

            valor1 = valor1+2

    print()

    cont = int(input("Digite 0 para interromper a execução: "))
