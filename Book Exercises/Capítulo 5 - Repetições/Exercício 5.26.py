cont1 = 1

while cont1 != 0:

    print()

    print("Digite dois números a seguir para saber o resto divisão inteira entre eles")

    print()

    valor1 = float(input("Digite um número: "))

    valor2 = float(input("Digite outro número: "))

    soma = 0

    cont = 0

    valor3 = valor2

    valor4 = valor1

    while cont != 1:

        if valor1 > valor2:

            valor2 = 0

            while valor2 < valor1:

                cont = cont+1

                valor2 += valor3

                if valor2+valor3 > valor1:

                    break

            print()

            soma = cont

            print("O resto inteiro da divisão entre %d e %d é: %d" % (valor1, valor3, soma))

            cont = 1

        elif valor1 < valor2:

            valor1 = 0

            while valor1 < valor2:

                cont = cont+1

                valor1 += valor3

                if valor1+valor3 > valor2:

                    break

            print()

            print("O resto inteiro da divisão entre %d e %d é: %d" % (valor4, valor2, soma))

            cont = 1

        elif valor1 == valor2:

            soma = (valor1-valor2)+1

            print()

            print("O resto inteiro da divisão entre %d e %d é: %d" % (valor1, valor2, soma))

            cont = 1

    print()

    cont1 = int(input("Digite 0 para interromper a execução, ou qualquer outro número inteiro para repiti-la: "))

    print()
