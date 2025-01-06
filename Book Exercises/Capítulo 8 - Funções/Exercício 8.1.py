def maior_menor_valor(numero1: float, numero2: float):

    if numero1 > numero2:

        return "O valor %s é maior que %d" % (numero1, numero2)

    elif numero1 < numero2:

        return "O valor %s é maior que %d" % (numero2, numero1)

    elif numero1 == numero2:

        return "Valores equivalentes!"

print(maior_menor_valor(6, 8))