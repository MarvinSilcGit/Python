def gerador_tabuada_simples (numero_tabuada: int):

    for contador in range(1, 10 + 1):

        print("%d x %d = %d " % (numero_tabuada, contador, numero_tabuada * contador))

    return 0


def gerador_tabuada_inicio_fim (numero_inicial: int, numero_final: int):

    for contador in range(1, numero_final + 1):

        print("%d x %d = %d " % (numero_inicial, contador, numero_inicial * contador))

    return 0


def gerador_tabuada_inicio_fim_razao (numero_inicial: int, numero_final: int, razao: int):

    for contador in range(1, numero_final + 1, razao):

        print("%d x %d = %d " % (numero_inicial, contador, numero_inicial * contador))

    return 0
