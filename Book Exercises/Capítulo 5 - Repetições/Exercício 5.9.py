contador1 = 1

contador2 = 0

restoInteiro = 0

resto = 0

while contador1 != 0:

    valor1 = float(input("Digite o primeiro valor: "))

    valor2 = float(input("Digite o segundo valor: "))

    print()

    while True:

        restoInteiro += valor2

        contador2 += 1

        if restoInteiro + valor2 == valor1:

            restoInteiro = contador2 + 1

            contador2 = 0

            break

    print("O resto inteiro da divisão entre %d e %d é %d e o resto da divisão é: %d" % (valor1, valor2, restoInteiro, resto))

    print()

    contador1 = int(input("Digite 0 para interromper a execução: "))

    print()