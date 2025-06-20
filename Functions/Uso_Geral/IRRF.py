def desconto_irrf (salario: float):

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