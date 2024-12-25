cont = 1

while cont != 0:
    
    deposito = float(input("Qual o valor do depósito inicial na conta? "))

    mensal = float(input("Qual o valor depositado mensalmente? "))

    taxa = float(input("Qual a taxa de juros da poupança no período? "))

    cont = 1

    ganho = 0

    while cont <= 24:

        ganho = (deposito)+(deposito/100)*taxa

        if ganho > deposito:

            print("O valor do depósito no %d° mês era de %.2f, com uma taxa de %.2f por cento, resultando no valor de %.2f R$ reais " % (cont, deposito, taxa, ganho))

            deposito = ganho

            cont = cont+1

            deposito = deposito+mensal

        elif ganho == deposito:

            print("No mês %d não teve aumento em relação ao mês anterior na poupança" % cont)

            deposito = ganho

            cont = cont+1

        elif ganho < deposito:

            print("No mês %d teve uma redução de %.2f para %2.f, em relação ao mês passado" % (cont, deposito, ganho))

            deposito = ganho

            cont = cont+1

    print()

    cont = int(input("Digite 0 para interromper a execução: "))

    print()
