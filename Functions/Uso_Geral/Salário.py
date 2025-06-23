from INSS import desconto_inss

from IRRF import desconto_irrf


def salario_liquido (salario: float):
    """Função responável por calcular o salário líquido no ano de 2025."""
    salario_final = salario

    salario_final -= desconto_inss(salario)

    salario_final -= desconto_irrf(salario)

    return f"{salario_final:.2f}"