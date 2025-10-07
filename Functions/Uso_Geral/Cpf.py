def formatar_cpf (cpf: str):
    """Função responsável por formatar o número do CPF."""
    if len(cpf) == 11:

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

    else:

        return 'CPF inválido'


def validar_cpf (cpf: str):
    """Função responsável por verificar a validade do número do CPF."""
    try:

        cpf_convertido = list(str(cpf))

        cpf = int(cpf)

    except ValueError:

        return 'Somente números são permitidos'

    else:

        cpf_validador = cpf_convertido[0:9]

        resultado_posicao_j = 0

        resultado_posicao_k = 0

        contador = 10

        lista_posicoes_cpf = [resultado_posicao_j, resultado_posicao_k]

        for contador2 in lista_posicoes_cpf:

            for contador3 in cpf_validador:

                lista_posicoes_cpf[contador2] += int(contador3) * contador

                contador -= 1

            if lista_posicoes_cpf[contador2] % 11 < 2:

                cpf_validador += '0'

            elif 2 <= lista_posicoes_cpf[contador2] % 11 <= 10: # equals to: elif lista_posicoes[contador2] % 11 >= 2 and lista_posicoes[contador2]  % 11 <= 10:

                cpf_validador += str(11 - (lista_posicoes_cpf[contador2] % 11))

            contador = 11

        if cpf_convertido == cpf_validador:

            return True

        else:

            return False
print(validar_cpf('28754564824'))

def gerador_cpf ():
    """Função responsável por gerar CPFs aleatórios."""
    import random as aleatoriedade

    cpf = ''

    for contador in range(11):

        cpf += str(aleatoriedade.randint(0,9))

    cpf = formatar_cpf(cpf)

    return cpf


def local_emissao_cpf (cpf: str):
    """Função responsável por informar o local de emissão do CPF."""
    dicionario_estados = {"1": "Distrito Federal, Goiás, Mato Grosso do Sul ou Tocantins", "2": "Pará, Amazonas, Acre, Amapá, Rondônia ou Roraíma",
                          "3": "Ceará, Maranhão ou Piauí",
                          "4": "Pernambuco, Rio Grande do Norte, Paraíba ou Alagoas", "5": "Bahia ou Sergipe", "6": "Minas Gerais",
                          "7": "Rio de Janeiro ou Espírito Santo", "8": "São Paulo",
                          "9":"Paraná ou Santa Catarina"}


    return f'O CPF foi emitido em: {dicionario_estados.get(cpf[8])}'