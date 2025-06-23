def estado_ddd (ddd):
    """Função que armazena a lista de ddd do Brasil e sua respectiva região."""
    dict_ddd_estado = {"68": "Acre", "96": "Amapá", "92": "Amazonas", "97": "Amazonas", "91": "Pará",
                             "93": "Pará", "94": "Pará", "69": "Rondônia", "95": "Roraima", "63": "Tocantins",
                             "61": "Distrito Federal", "62": "Goiás", "64": "Goiás", "65": "Mato Grosso",
                             "66": "Mato Grosso", "67": "Mato Grosso do Sul", "82": "Alagoas", "71": "Bahia",
                             "73": "Bahia", "74": "Bahia", "75": "Bahia", "77": "Bahia", "79": "Sergipe",
                             "85": "Ceará", "88": "Ceará", "98": "Maranhão", "99": "Maranhão", "83": "Paraíba",
                             "81": "Pernambuco", "87": "Pernambuco", "86": "Piauí", "89": "Piauí", "84": "Rio Grande do Norte",
                             "27": "Espírito Santo", "28": "Espírito Santo", "31": "Minas Gerais", "32": "Minas Gerais",
                             "33": "Minas Gerais", "34": "Minas Gerais", "35": "Minas Gerais", "37": "Minas Gerais",
                             "38": "Minas Gerais", "21": "Rio de Janeiro", "22": "Rio de Janeiro", "24": "Rio de Janeiro",
                             "11": "São Paulo", "12": "São Paulo", "13": "São Paulo", "14": "São Paulo", "15": "São Paulo",
                       "16": "São Paulo", "17": "São Paulo", "18": "São Paulo", "19": "São Paulo", "41": "Paraná",
                       "42": "Paraná", "43": "Paraná", "44": "Paraná", "45": "Paraná", "46": "Paraná", "51": "Rio Grande do Sul",
                       "53": "Rio Grande do Sul", "54": "Rio Grande do Sul", "55": "Rio Grande do Sul", "47": "Santa Catarina",
                       "48": "Santa Catarina", "49": "Santa Catarina"}

    if not ddd in dict_ddd_estado:

        return False

    else:

        return dict_ddd_estado[ddd]


def lista_ddd():
    """Função que armazena a lista de ddd do Brasil."""
    ddd = ['11', '12', '13', '14', '15', '17', '16', '17', '18', '19', '21', '22', '24', '27', '28', '31',
                 '32', '33', '34', '35', '37', '38', '41', '42', '43', '44', '45', '46', '47', '48', '49', '51',
                 '53', '54', '55', '61', '62', '63', '64', '65', '66', '67', '68', '71', '73', '74', '75', '77',
                 '79', '81', '82', '83', '84', '85', '86', '87', '88', '89', '91', '92', '93', '94', '95', '96',
                 '97', '98', '99']

    return ddd


def formatar_numero_telefone_movel (numero: str):
    """Função responsável por formatar o número de telefone móvel para o padrão brasileiro."""
    if not estado_ddd(numero[0:2]) or len(numero) != 11:

        return "Número inválido"

    else:

        numero_movel_formatado = list(numero)

        for contador in range(11):

            if contador == 0:

                numero_movel_formatado.insert(contador, '(')

            elif contador == 3:

                numero_movel_formatado.insert(contador, ')')

            elif contador == 4:

                numero_movel_formatado.insert(contador, ' ')

            elif contador == 10:

                numero_movel_formatado.insert(contador, '-')

        numero_movel_formatado = ''.join(numero_movel_formatado)

        return f"{numero_movel_formatado}"


def gerador_numero_telefone_movel ():
    """Função responsável por gerar números móveis aleatórios."""
    import random as aleatorio

    numero_telefone_movel = ''

    for contador in range(9):

        if len(numero_telefone_movel) == 0:

            numero_telefone_movel += aleatorio.choice(lista_ddd())

        elif len(numero_telefone_movel) == 2:

            numero_telefone_movel += '9'

        elif len(numero_telefone_movel) == 3:

            bandas_prefixo = ['80', '81', '82', '83', '84', '85', '86', '87', '88', '91', '92', '93', '94', '96', '97', '98', '99']

            numero_telefone_movel += aleatorio.choice(bandas_prefixo)

        else:

            numero_telefone_movel += str(aleatorio.randint(0, 9))

    return formatar_numero_telefone_movel(numero_telefone_movel)


def formatar_numero_telefone_fixo (numero: str):
    """Função responsável por formatar o número de telefone fixo para o padrão brasileiro."""
    if not estado_ddd(numero[0:2]) or len(numero) != 10:

        return "Número inválido"

    else:

        numero_fixo_formatado = list(numero)

        for contador in range(10):

            if contador == 0:

                numero_fixo_formatado.insert(contador, '(')

            elif contador == 3:

                numero_fixo_formatado.insert(contador, ')')

            elif contador == 4:

                numero_fixo_formatado.insert(contador, ' ')

            elif contador == 9:

                numero_fixo_formatado.insert(contador, '-')

        numero_fixo_formatado = ''.join(numero_fixo_formatado)

        return f"{numero_fixo_formatado}"


def gerador_numero_telefone_fixo ():
    """Função responsável por gerar números fixos aleatórios."""
    import random as aleatorio

    numero_telefone_fixo = ''

    for contador in range(9):

        if len(numero_telefone_fixo) == 0:

            numero_telefone_fixo += aleatorio.choice(lista_ddd())

        elif len(numero_telefone_fixo) == 2:

            numero_telefone_fixo += str(aleatorio.randrange(2, 5))

        else:

            numero_telefone_fixo += str(aleatorio.randrange(0, 9))

    return formatar_numero_telefone_fixo(numero_telefone_fixo)