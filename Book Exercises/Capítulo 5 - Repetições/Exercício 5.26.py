contador1 = 1

while contador1 != 0:

    restoInteiro = 0

    resto = 0

    valor1 = float(input("Digite o primeiro valor: "))

    valor2 = float(input("Digite o segundo valor: "))

    if valor1 == 0 or valor2 == 0:

        print("Divisão por zero inválida")

        print()

        continue

    else:

        if valor1 == valor2:

            restoInteiro = 1

            print()

        elif valor1 > valor2:

            while valor2 + resto < valor1:

                restoInteiro += 1

                resto += valor2

            resto = valor1 - resto

        else:

            while valor1 + resto < valor2:

                resto += valor1

            while resto != valor2:

                resto += 1

        print("O resto da divisão entre %.1f e %.1f é: %.1f" % (valor1, valor2, resto))

        print()

        contador1 = int(input("Digite 0 para interromper a execução: "))

        print()