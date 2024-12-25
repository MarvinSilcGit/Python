contador = 1

resultado = 0

while contador != 0:

    valor1 = int(input("Digite um valor: "))

    valor2 = int(input("Digite outro valor: "))

    for contador2 in range(0, valor2):

        print("%d + %d = %d" % (resultado, valor1, resultado + valor1))

        resultado += valor1

    print()

    contador = int(input("Digite 0 para interromper a execução: "))