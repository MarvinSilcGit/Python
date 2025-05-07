def gerador_tabuada_simples (numero_tabuada: int):

    for contador in range(1, 10 + 1):

        print(f"{numero_tabuada:d} x {contador:d} = numero_tabuada * contador")

    return 0


def gerador_tabuada_inicio_fim (numero_inicial: int, numero_final: int):

    for contador in range(1, numero_final + 1):

        print(f"{numero_inicial:d} x {contador:d} = numero_tabuada * contador")

    return 0


def gerador_tabuada_inicio_fim_razao (numero_inicial: int, numero_final: int, razao: int):

    for contador in range(1, numero_final + 1, razao):

        print(f"{numero_inicial:d} x {contador:d} = numero_tabuada * contador")

    return 0