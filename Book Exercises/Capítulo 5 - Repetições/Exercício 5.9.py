contador1 = 1

restoInteiro = 0

resto = 0

while contador1 != 0:

    valor1 = float(input("Digite o primeiro valor: "))

    valor2 = float(input("Digite o segundo valor: "))

    if valor1 == valor2:

        restoInteiro = (valor1 - valor2) + 1

        resto = valor1 - valor2

        print()

        print("O resto inteiro da divisão entre %d e %d é: %d. E o resto da divisão é: %d" % (valor1, valor2, restoInteiro, resto))

        restoInteiro = 0

    elif valor1 > valor2:

        resto = 0

        while valor1 > resto:

            restoInteiro += 1

            resto += valor2

            if valor2 + resto > valor1:

                break

        resto = valor1 - resto

        print("O resto inteiro da divisão entre %d e %d é: %d. E o resto da divisão é: %d" % (valor1, valor2, restoInteiro, resto))

        restoInteiro = 0

        resto = 0

    else:

        while valor2 > resto:

            resto += valor1

            if valor1 + resto > valor2:

                break

        while resto != valor2:

            resto += 1

            if resto == valor2:

                break

        restoInteiro = 0

        print("O resto inteiro da divisão entre %d e %d é: %d. E o resto da divisão é: %d" % (valor1, valor2, restoInteiro, resto))

        resto = 0

    print()

    contador1 = int(input("Digite 0 para interromper a execução: "))

    print()