contador = 0

while contador != 1:

    valor1 = int(input("Digite um valor: "))

    valor2 = int(input("Digite outro valor: "))

    for contador2 in range(valor1, valor2):

        valor1 += valor2

        print(valor1)

    print()

    contador = int(input("Digite 0 para interromper a execução: "))