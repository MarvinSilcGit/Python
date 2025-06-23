def desconto_inss (salario_mensal: float):

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

    return f"{desconto:.2f}"