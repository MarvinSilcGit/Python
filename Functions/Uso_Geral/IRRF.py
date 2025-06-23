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

        return f"{desconto:.2f}"

    else:

        return 0

# FIXME: NOT GOOD ABOVE 5K