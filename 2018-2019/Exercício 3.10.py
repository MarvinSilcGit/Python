salario = float(input("digite o salário recebido anualmente: "))

porcentagem = float(input("qual a porcentagem de aumento? "))

aumento = (porcentagem / 10) * (salario / 10)

total = salario + aumento

print("com um salario inicial de R$ %.2f e um aumento de R$ %.2f, o funcionario passará à receber R$ %.2f" % (salario, aumento, total))
