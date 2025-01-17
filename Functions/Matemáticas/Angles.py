def radiano_graus (radiano: float):

    import math

    graus = radiano * 180 / math.pi

    return  "%.2f radianos equivalem à %.2f° Graus" % (radiano, graus)


def radiano_grados (radiano: float):

    import math

    grados = radiano * 200 / math.pi

    return  "%.2f radianos equivalem à %.2f° Grados" % (radiano, grados)


def graus_radiano (grau: float):

    import math

    radiano = grau * math.pi / 180

    return "%.2f° Graus equivalem à %.3f Radianos" % (grau, radiano)


def graus_grados (graus: float):

    grados = graus * 200 / 180

    return "%.2f° Graus equivalem à %.2f° Grados" % (graus, grados)


def grados_radiano (grado: float):

    import math

    radiano = grado * math.pi / 200

    return "%.2f° Grados equivalem à %.2f° Radianos" % (grado, radiano)


def grados_graus (grado: float):

    graus = grado / 100 * 90

    return "%.2f° Grados equivalem à %.2f° Graus" % (grado, graus)