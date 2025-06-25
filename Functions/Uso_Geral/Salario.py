def desconto_inss (salario_mensal: float):
    """Função responável por calcular o desconto do inss sobre o salário no ano de 2025."""
    faixas_inss = {0: 1518, 1: 1275.88, 2: 1396.94, 3: 3966.57}

    aliquotas_inss = {0: 7.5, 1: 9, 2: 12, 3: 14}

    desconto = 0

    faixa_salarial = salario_mensal

    contador = 0

    while faixa_salarial > 0:

        if faixa_salarial <= faixas_inss.get(contador):

            desconto += faixa_salarial / 100 * aliquotas_inss.get(contador)

        else:

            desconto += faixas_inss.get(contador) / 100 * aliquotas_inss.get(contador)

        faixa_salarial -= faixas_inss.get(contador)

        contador += 1

        if contador > 3:

            break

    return desconto


def desconto_irrf (salario: float):
    """Função responável por calcular o desconto do irrf sobre o salário no ano de 2025."""
    salario = salario - 607.20

    desconto = 0

    if salario > 2428.80:

        if salario <= 2826.65:

            desconto += salario / 100 * 7.5

            desconto -= 182.16

        elif salario <= 3751.05:

            desconto += salario / 100 * 15

            desconto -= 394.16

        elif salario <= 4664.68:

            desconto = salario / 100 * 22.5

            desconto -= 675.49

        else:

            desconto = salario / 100 * 27.5

            desconto -= 908.73

        return desconto

    else:

        return 0

# FIXME: NOT GOOD ABOVE 5K

def salario_liquido (salario: float):
    """Função responável por calcular o salário líquido no ano de 2025."""
    inss = desconto_inss(salario)

    irrf = desconto_irrf(salario)

    salario_final = salario - inss - irrf

    return salario_final

sl = salario_liquido(6512)
print(f"{sl:.2f}")