def formatar_cpf (cpf: str):

    cpf = list(cpf)

    for contador in range(14):

        if contador == 3:

            cpf.insert(contador, '.')

        elif contador == 7:

            cpf.insert(contador, '.')

        elif contador == 11:

            cpf.insert(contador, '-')

    cpf = ''.join(cpf)

    return cpf


def validar_cpf (cpf):

    cpf_validador = list(cpf[0:9])

    cpf_validador = ''.join(cpf_validador)

    dicionario_estados = {"1": "Distrito Federal, Goiás, Mato Grosso do Sul ou Tocantins", "2": "Pará, Amazonas, Acre, Amapá, Rondônia ou Roraíma",
                          "3": "Ceará, Maranhão ou Piauí",
                          "4": "Pernambuco, Rio Grande do Norte, Paraíba ou Alagoas", "5": "Bahia ou Sergipe", "6": "Minas Gerais",
                          "7": "Rio de Janeiro ou Espírito Santo", "8": "São Paulo",
                          "9":"Paraná ou Santa Catarina"}

    resultado_posicao_j = 0

    resultado_posicao_k = 0

    contador = 10

    for contador2 in cpf_validador:

        resultado_posicao_j += int(contador2) * contador

        contador -= 1

    if resultado_posicao_j % 11 < 2:

        cpf_validador += '0'

    elif 2 <= resultado_posicao_j % 11 <= 10: # equals to: elif resultado_posicao_j >= 2 and resultado_posicao_j <= 10:

        cpf_validador += str(11 - (resultado_posicao_j % 11))

    contador = 11

    for contador2 in cpf_validador:

        resultado_posicao_k += int(contador2) * contador

        contador -= 1

    if resultado_posicao_k % 11 < 2:

        cpf_validador += '0'

    elif 2 <= resultado_posicao_k % 11 <= 10: # equals to: elif resultado_posicao_k >= 2 and resultado_posicao_k <= 10:

        cpf_validador += str(11 - (resultado_posicao_k % 11))

    if cpf == cpf_validador:

        return f"O Uso_Geral {formatar_cpf(cpf)} é válido, sendo emitido em {dicionario_estados[cpf[8]]}"

    else:

        return "Uso_Geral inválido"


def gerador_cpf ():

    import random as aleatoriedade

    cpf = ''

    for contador in range(11):

        cpf += str(aleatoriedade.randint(0,9))

    cpf = formatar_cpf(cpf)

    return cpf