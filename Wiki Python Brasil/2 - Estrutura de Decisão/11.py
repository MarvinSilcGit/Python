salario_inicial = float(input("Digite o salário atual: "))

aumento = 0

salario_final = salario_inicial

if salario_inicial <= 280:

    aumento = salario_inicial / 100 * 20

    salario_final += aumento

    print("O salário antes do reajuste era de R$ %.2f e passou a ser R$ %.2f com um aumento de R$ %.2f, ou um aumento de 20 por cento" % (salario_inicial, salario_final, aumento,))

elif salario_inicial <= 700:

    aumento = salario_inicial / 100 * 15

    salario_final += aumento

    print("O salário antes do reajuste era de R$ %.2f e passou a ser R$ %.2f com um aumento de R$ %.2f, ou um aumento de 15 por cento" % (salario_inicial, salario_final, aumento,))

elif salario_inicial <= 1500:

    aumento = salario_inicial / 100 * 10

    salario_final += aumento

    print("O salário antes do reajuste era de R$ %.2f e passou a ser R$ %.2f com um aumento de R$ %.2f, ou um aumento de 10 por cento" % (salario_inicial, salario_final, aumento,))

elif salario_inicial > 1500:

    aumento = salario_inicial / 100 * 5

    salario_final += aumento

    print("O salário antes do reajuste era de R$ %.2f e passou a ser R$ %.2f com um aumento de R$ %.2f, ou um aumento de 5 por cento" % (salario_inicial, salario_final, aumento,))