def maior_valor(x: float, w:float):

    if x > w:

        return "O valor %s é maior!" % x

    elif x < w:

        return "O valor %s é maior!" % w

    elif x == w:

        return "Valores equivalentes!"

print(maior_valor(6, 8))