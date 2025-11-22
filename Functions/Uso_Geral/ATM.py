from Functions.Calculadoras.Validations import validade_numero_decimal

def atm_machine (valor_saque: int):
    """Função responsável por imitar a função saque de um caixa eletrônico."""
    resultado = []

    try:

        valor_saque = int(valor_saque)

    except ValueError:

        return 'Não são permitidos letras ou números decimais'

    else:

        dict_contagem_cedulas = {200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

        lista_cedulas = [200, 100, 50, 20, 10, 5, 2, 1]

        contador = 0

        while valor_saque != 0:

            if valor_saque >= lista_cedulas[contador]:

                valor_saque -= lista_cedulas[contador]

                resultado.append(lista_cedulas[contador])

            else:

                contador += 1

        for _ in dict_contagem_cedulas:

            dict_contagem_cedulas.update({_: resultado.count(_)})

        return dict_contagem_cedulas

#How to access the function

#quantidade_saque = input("Digite o valor de saque: ")

#lista = atm_machine(quantidade_saque)

#for _ in lista:

#   print(f"{lista[_]} cédulas de {_}" if lista[_] > 1 else f"{lista[_]} cédula de {_}")

#print(atm_machine)