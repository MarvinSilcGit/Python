def gerador_tabuada_simples (numero_tabuada: int):
    """Função responsável por geral uma tabuada simples. Começa sempre por 1 e o último número precisa ser passado como parâmetro."""
    for contador in range(1, 10 + 1):

        print(f"{numero_tabuada:d} x {contador:d} = {numero_tabuada * contador}")

    return ''


def gerador_tabuada_inicio_fim (numero_inicial: int, numero_final: int):
    """Função responsável por gerar uma tabuada intermediária. O primeiro parâmetro é o início e o último é o fim."""
    for contador in range(1, numero_final + 1):

        print(f"{numero_inicial:d} x {contador:d} = {numero_inicial * contador}")

    return ''


def gerador_tabuada_inicio_fim_razao (numero_inicial: int, numero_final: int, razao: int):
    """Função responsável por gerar uma tabuada Avançada. O primeiro parâmetro é o início, o segundo parâmetro é o fim e o terceiro parâmetro é a razão."""
    for contador in range(1, numero_final + 1, razao):

        print(f"{numero_inicial:d} x {contador:d} = {numero_inicial * contador}")

    return ''