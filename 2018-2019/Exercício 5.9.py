cont = 1

cont2 = 0

while cont != 0:

    valor1 = float(input("Digite o primeiro valor: "))

    valor2 = float(input("Digite o segundo valor: "))

    if valor1 == valor2:

        soma = (valor1-valor2)+1

        resto = valor1-valor2

        print()

        print("O resto inteiro da divisão entre %d e %d  é: %d. E o resto da divisão é: %d" % (valor1, valor2, soma,resto))

    elif valor1 > valor2:

        valor3 = 0

        while valor1 > valor3:

            cont2 += 1

            valor3 += valor2

            if valor2+valor3 > valor1:

                break

        valor3 = valor1-valor3

        print("O resto inteiro da divisão entre %d e %d é: %d. E o resto da divisão é: %d" % (valor1, valor2, cont2, valor3))

        cont2 = 0

        valor3 = 0

    elif valor2 > valor1:

        valor3 = 0

        while valor2 > valor3:

            cont2 += 1

            valor3 += valor1

            if valor1+valor3 > valor2:

                break

        while valor3 != valor2:

            valor3 += 1

            if valor3 == valor2:

                break

        cont2 = 0

        print("O resto inteiro da divisão entre %d e %d é: %d. E o resto da divisão é: %d" % (valor1, valor2, cont2, valor3))

        cont2 = 0

        valor3 = 0

    print()

    cont = int(input("Digite 0 para interromper a execução: "))

    print()
