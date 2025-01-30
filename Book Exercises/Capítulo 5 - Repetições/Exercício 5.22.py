contador1 = 1

while contador1 != 0:

    print("Escolha dentre as opções abaixo: ")

    print()

    print("Digite 1 para somar: ")

    print("Digite 2 para subtrair: ")

    print("Digite 3 para dividir: ")

    print("Digite 4 para multiplicar: ")

    print()

    math_operator = int(input("Digite o valor correspondente para a operação desejada: "))

    print()

    if math_operator != 1 and math_operator != 2 and math_operator != 3 and math_operator != 4:

        print("Opção inexistente")

        continue

    else:

        valor1 = float(input("Digite o primeiro valor: "))

        valor2 = float(input("Digite o segundo valor: "))

        print()

        if math_operator == 1:

            print("O resultado da soma é: %.1f" % (valor1 + valor2))

        elif math_operator == 2:

            print("O resultado da subtração é: %.1f" % (valor1 - valor2))

        elif math_operator == 3:

            print("O resultado da divisão é: %.1f" % (valor1 / valor2))

        elif math_operator == 4:

            print("O resultado da multiplicação é: %.1f" % (valor1 * valor2))

    print()

    contador1 = int(input("Digite 0 para interromper a execução: "))

    print()