salario = float(input("digite o salário recebido anualmente: "))

porcentagem = float(input("qual a porcentagem de aumento? "))

aumento = (porcentagem/10)*(salario/10)

total = salario+aumento

print("com um salario inicial de %d R$ e um aumento de %d R$, o funcionario passará à receber %d R$" % (salario, aumento, total))
