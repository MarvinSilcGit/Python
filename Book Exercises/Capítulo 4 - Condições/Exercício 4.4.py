salario = float(input("Qual o seu salário? "))

if salario > 1250:

    aumento1 = salario / 10

    salarioFinal = salario + aumento1

    print("O salário  de R$ %.2f passará a ser de R$ %.2f, com um aumento de R$ %.2f" % (salario, salarioFinal, aumento1))

else:

    if salario <= 1250:

        aumento1 = salario * 0.15

        salarioFinal = salario + aumento1

        print("O salário de R$ %.2f passará a ser de R$ %.2f, com um aumento de R$ %.2f" % (salario, salarioFinal, aumento1))
