cont1 = 1

while cont1 != 0:

    print("Escolha dentre as opções abaixo: ")

    print()

    print("Digite 1 para somar: ")

    print("Digite 2 para subtrair: ")

    print("Digite 3 para dividir: ")

    print("Digite 4 para multiplicar: ")

    print()

    valor = int(input("Digite o valor correspondente para a operação desejada: "))

    print()

    if valor == 1:

        valor1 = float(input("Digite o primeiro valor: "))

        valor2 = float(input("Digite o segundo valor: "))

        print()

        print("O resultado da soma é: %.1f" % (valor1+valor2))

    elif valor == 2:

        valor1 = float(input("Digite o primeiro valor: "))

        valor2 = float(input("Digite o segundo valor: "))

        print()

        print("O resultado da subtração é: %.1f" % (valor1-valor2))

    elif valor == 3:

        valor1 = float(input("Digite o primeiro valor: "))

        valor2 = float(input("Digite o segundo valor: "))

        print()

        print("O resultado da divisão é: %.1f" % (valor1/valor2))

    elif valor == 4:

        valor1 = float(input("Digite o primeiro valor: "))

        valor2 = float(input("Digite o segundo valor: "))

        print()

        print("O resultado da multiplicação é: %.1f" % (valor1*valor2))

    elif valor != 1 and valor != 2 and valor != 3 and valor != 4:

        print("opção inexistente")

        break

    print()

    cont1 = int(input("Digite 0 para interromper a execução: "))

    print()
