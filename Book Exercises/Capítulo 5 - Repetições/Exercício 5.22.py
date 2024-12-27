contador1 = 1

while contador1 != 0:

    print("Escolha dentre as opções abaixo: ")

    print()

    print("Digite 1 para somar: ")

    print("Digite 2 para subtrair: ")

    print("Digite 3 para dividir: ")

    print("Digite 4 para multiplicar: ")

    print()

    mathOperator = int(input("Digite o valor correspondente para a operação desejada: "))

    print()

    if mathOperator == 1:

        valor1 = float(input("Digite o primeiro valor: "))

        valor2 = float(input("Digite o segundo valor: "))

        print()

        print("O resultado da soma é: %.1f" % (valor1 + valor2))

    elif mathOperator == 2:

        valor1 = float(input("Digite o primeiro valor: "))

        valor2 = float(input("Digite o segundo valor: "))

        print()

        print("O resultado da subtração é: %.1f" % (valor1 - valor2))

    elif mathOperator == 3:

        valor1 = float(input("Digite o primeiro valor: "))

        valor2 = float(input("Digite o segundo valor: "))

        print()

        print("O resultado da divisão é: %.1f" % (valor1 / valor2))

    elif mathOperator == 4:

        valor1 = float(input("Digite o primeiro valor: "))

        valor2 = float(input("Digite o segundo valor: "))

        print()

        print("O resultado da multiplicação é: %.1f" % (valor1 * valor2))

    elif mathOperator != 1 and mathOperator != 2 and mathOperator != 3 and mathOperator != 4:

        print("Opção inexistente")

        break

    print()

    contador1 = int(input("Digite 0 para interromper a execução: "))

    print()