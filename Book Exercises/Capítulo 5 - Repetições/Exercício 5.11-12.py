contador1 = 1

while contador1 != 0:
    
    depositoInicial = float(input("Qual o valor do depósito inicial na conta? "))

    depositoMensal = float(input("Qual o valor depositado mensalmente? "))

    taxaJuros = float(input("Qual a taxa de juros da poupança no período? "))

    ganhoTotal = 0

    for contador2 in range(24):

        ganhoTotal = depositoInicial + (depositoInicial / 100) * taxaJuros

        if ganhoTotal > depositoInicial:

            print("O valor do depósito no %d° mês era de %.2f, com uma taxa de %.2f por cento, resultando no valor de %.2f R$ reais " % (contador2, depositoInicial, taxaJuros, ganhoTotal))

            depositoInicial = ganhoTotal

            contador1 += 1

            depositoInicial = depositoInicial + depositoMensal

        elif ganhoTotal == depositoInicial:

            print("No mês %d não teve aumento em relação ao mês anterior na poupança" % contador2)

            depositoInicial = ganhoTotal

            contador1 += 1

        elif ganhoTotal < depositoInicial:

            print("No mês %d teve uma redução de %.2f para %2.f, em relação ao mês passado" % (contador2, depositoInicial, ganhoTotal))

            depositoInicial = ganhoTotal

            contador1 += 1

    print()

    contador1 = int(input("Digite 0 para interromper a execução: "))

    print()