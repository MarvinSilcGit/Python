def desconto_irrf (salario_mensal: float):

    faixas_irrf = {0: 397.84, 1: 924.39, 2: 913.62}

    aliquotas_irrf = {0: 15, 1: 22.5, 2: 27.5}

    desconto = 0

    faixa_salarial = salario_mensal

    contador = 0

    limite_insencao = 3036

    faixa_salarial -= limite_insencao

    if salario_mensal > limite_insencao:

        while faixa_salarial > 0:

            if faixa_salarial <= faixas_irrf.get(contador):

                desconto += faixa_salarial / 100 * aliquotas_irrf.get(contador)

            else:

                desconto += faixas_irrf.get(contador) / 100 * aliquotas_irrf.get(contador)

            faixa_salarial -= faixas_irrf.get(contador)

            contador += 1

            if contador > 2:

                break

    return desconto