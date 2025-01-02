salarioInicial = float(input("Digite o salário atual: "))

aumento = 0

salarioFinal = salarioInicial

if salarioInicial <= 280:

    aumento = salarioInicial / 100 * 20

    salarioFinal += aumento

    print("O salário antes do reajuste era de R$ %.2f e passou a ser R$ %.2f com um aumento de R$ %.2f, ou um aumento de 20 por cento" % (salarioInicial, salarioFinal, aumento,))

elif salarioInicial <= 700:

    aumento = salarioInicial / 100 * 15

    salarioFinal += aumento

    print("O salário antes do reajuste era de R$ %.2f e passou a ser R$ %.2f com um aumento de R$ %.2f, ou um aumento de 15 por cento" % (salarioInicial, salarioFinal, aumento,))

elif salarioInicial <= 1500:

    aumento = salarioInicial / 100 * 10

    salarioFinal += aumento

    print("O salário antes do reajuste era de R$ %.2f e passou a ser R$ %.2f com um aumento de R$ %.2f, ou um aumento de 10 por cento" % (salarioInicial, salarioFinal, aumento,))

elif salarioInicial > 1500:

    aumento = salarioInicial / 100 * 5

    salarioFinal += aumento

    print("O salário antes do reajuste era de R$ %.2f e passou a ser R$ %.2f com um aumento de R$ %.2f, ou um aumento de 5 por cento" % (salarioInicial, salarioFinal, aumento,))