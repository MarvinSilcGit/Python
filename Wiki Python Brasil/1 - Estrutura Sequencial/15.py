salario = float(input("Digite o seu salário: "))

salario_liquido = salario

salario_liquido -= salario / 100 * 11

salario_liquido -= salario_liquido / 100 * 8

salario_liquido -= salario_liquido / 100 * 5

print(f"O salário líquido será R$ {salario_liquido:.2f}, com R$ {salario - salario_liquido:.2f} de desconto")