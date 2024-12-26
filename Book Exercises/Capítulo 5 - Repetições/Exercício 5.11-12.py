contador1 = 1

while contador1 != 0:
    
    depositoInicial = float(input("Qual o valor do depósito inicial na conta? "))

    depositoMensal = float(input("Qual o valor depositado mensalmente? "))

    taxaJuros = float(input("Qual a taxa de juros da poupança no período? "))

    contador1 = 1

    ganho = 0

    for contador2 in range(24):

        ganho = depositoInicial + (depositoInicial / 100) * taxaJuros

        if ganho > depositoInicial:

            print("O valor do depósito no %d° mês era de %.2f, com uma taxa de %.2f por cento, resultando no valor de %.2f R$ reais " % (contador1, depositoInicial, taxaJuros, ganho))

            depositoInicial = ganho

            contador1 += 1

            depositoInicial = depositoInicial + depositoMensal

        elif ganho == depositoInicial:

            print("No mês %d não teve aumento em relação ao mês anterior na poupança" % contador1)

            depositoInicial = ganho

            contador1 += 1

        elif ganho < depositoInicial:

            print("No mês %d teve uma redução de %.2f para %2.f, em relação ao mês passado" % (contador1, depositoInicial, ganho))

            depositoInicial = ganho

            contador1 += 1

    print()

    contador1 = int(input("Digite 0 para interromper a execução: "))

    print()