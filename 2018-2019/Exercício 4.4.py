salario = float(input("Qual o seu salário? "))

if salario > 1250:

    aumento1 = salario/10

    salarioFinal = salario+aumento1

    print("O salário  de %.2f R$ passará a ser de %.2f R$, com um aumento de %.2f R$" % (salario, salarioFinal, aumento1))

else:

    if salario <= 1250:

        aumento1 = salario*0.15

        salarioFinal = salario+aumento1

        print("O salário de %.2f R$ passará a ser de %.2f R$, com um aumento de %.2f R$" % (salario, salarioFinal, aumento1))
