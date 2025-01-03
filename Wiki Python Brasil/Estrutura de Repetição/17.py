def calculo_fatorial (numero: int):

    numero = numero

    resultado_fatorial = numero

    for contador in range(numero, 1, -1):

        resultado_fatorial *= contador - 1

    return "Fatorial de %d é %d" % (numero, resultado_fatorial)