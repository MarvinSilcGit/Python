contador1 = 1

while contador1 != 0:

    restoInteiro = 0

    resto = 0

    valor1 = float(input("Digite o primeiro valor: "))

    valor2 = float(input("Digite o segundo valor: "))

    if valor1 == valor2:

        restoInteiro = 1

        print()

    elif valor1 > valor2:

        while valor2 + resto < valor1:

            restoInteiro += 1

            resto += valor2

        resto = valor1 - resto

    else:

        while valor2 > resto:

            resto += valor1

            if valor1 + resto > valor2:

                break

        while resto != valor2:

            resto += 1

    print("O resto inteiro da divisão entre %d e %d é: %d. E o resto da divisão é: %d" % (valor1, valor2, restoInteiro, resto))

    print()

    contador1 = int(input("Digite 0 para interromper a execução: "))

    print()