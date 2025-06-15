from Functions.Calculadoras.Validations import validade_numero_decimal


def atm_machine (valor_pagamento: int):

    if validade_numero_decimal(valor_pagamento):

        return 'Valores não podem ser decimais'

    else:

        resultado = []

        dict_contagem_cedulas = {200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

        lista_cedulas = [200, 100, 50, 20, 10, 5, 2, 1]

        contador = 0

        while valor_pagamento != 0:

            if valor_pagamento >= lista_cedulas[contador]:

                valor_pagamento -= lista_cedulas[contador]

                resultado.append(lista_cedulas[contador])

            else:

                contador += 1

        for contador2 in dict_contagem_cedulas:

            dict_contagem_cedulas.update({contador2: resultado.count(contador2)})

        return dict_contagem_cedulas

"""
#How to acess values
valor_saque = int(input("Digite o valor de saque: "))

lista = atm_machine(valor_saque)

for cont in lista:

    print(f"{lista[cont]} cédulas de {cont}" if lista[cont] > 1 else f"{lista[cont]} cédula de {cont}")"""