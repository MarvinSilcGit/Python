salario = float(input("Digite o seu salário: "))

salarioLiquido = salario

salarioLiquido -= salario / 100 * 11

salarioLiquido -= salarioLiquido / 100 * 8

salarioLiquido -= salarioLiquido / 100 * 5

print("O salário líquido será R$ %.2f, com R$ %.2f de desconto" % (salarioLiquido, salario-salarioLiquido))