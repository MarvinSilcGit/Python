def formatar_cnpj (cnpj: str):

    cnpj = list(cnpj)

    for contador in range(18):

        if contador == 2:

            cnpj.insert(contador, '.')

        elif contador == 6:

            cnpj.insert(contador, '.')

        elif contador == 10:

            cnpj.insert(contador, '/')

        elif contador == 15:

            cnpj.insert(contador, '-')

    cnpj = ''.join(cnpj)

    return cnpj


def validar_cnpj(cnpj: str):

    cnpj_validador = list(cnpj[0:12])

    cnpj_validador = ''.join(cnpj_validador)

    resultado_posicao_x_1 = 0

    resultado_posicao_x_2 = 0

    contador = 5

    for contador2 in cnpj_validador:

        contador += 1

        posicao_x_1 = int(contador2)

        resultado_posicao_x_1 += posicao_x_1 * contador

        if contador == 9:

            contador = 1

    cnpj_validador += str(resultado_posicao_x_1 % 11)

    contador = 4

    for contador2 in cnpj_validador:

        contador += 1

        posicao_x_2 = int(contador2)

        resultado_posicao_x_2 += posicao_x_2 * contador

        if contador == 9:

            contador = 1

    cnpj_validador += str(resultado_posicao_x_2 % 11)

    cnpj_validador = formatar_cnpj(cnpj_validador)

    cnpj = formatar_cnpj(cnpj)

    if cnpj == cnpj_validador:

        return f"O CNPJ {cnpj} é válido"

    else:

        return f"O CNPJ {cnpj} é inválido"
#print(validar_cnpj('59120772000100')) FIXME: fazer funcionar onde o módulo do resultado da posicão é igual a 10

def gerador_cnpj ():

    import random as aleatoriedade

    cnpj = ''

    for contador in range(14):

        if contador == 8 or contador == 9 or contador == 10:

            cnpj += '0'

        elif contador == 11:

            cnpj += '1'

        else:

            cnpj += (str(aleatoriedade.randint(0,9)))

    cnpj = formatar_cnpj(cnpj)

    return cnpj