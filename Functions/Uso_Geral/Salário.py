from INSS import desconto_inss

from IRRF import desconto_irrf


def salario_liquido (salario: float):

    salario_final = salario

    salario_final -= desconto_inss(salario)

    salario_final -= desconto_irrf(salario_final)

    return salario_final


sl = salario_liquido(float(input("Digite seu salário: ")))

print(f"O seu salário líquido é: R$ {sl:,.2f}")