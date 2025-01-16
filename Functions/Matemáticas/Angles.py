def radiano_grau (radiano: float):

    import math

    return  "%.2f radianos equivalem à %.2f°" % (radiano, radiano * 180 / math.pi)


def grau_radiano (grau: float):

    import math

    return "%.2f° equivalem à %.3f radianos" % (grau, grau * math.pi / 180)