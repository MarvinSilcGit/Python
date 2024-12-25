cont = 1

while cont != 0:

    valor1 = int(input("digite um valor :"))

    valor2 = valor1+valor1

    while valor2 <= valor1*11:

        print(valor2)

        valor2 = valor2+valor1

    print()

    cont = int(input("Digite 0 para interromper a execução: "))

    if cont == 0:

        break
