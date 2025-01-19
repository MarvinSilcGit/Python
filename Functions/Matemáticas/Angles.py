import math

def radiano_graus (radiano: float):

    graus = radiano * 180 / math.pi

    return f"{radiano:,.2f}° Radianos equivalem à {graus:,.2f}° Graus"


def radiano_grados (radiano: float):

    grados = radiano * 200 / math.pi

    return f"{radiano:,.2f}° Radianos equivalem à {grados:,.2f}° Grados"


def graus_radiano (grau: float):

    radiano = grau * math.pi / 180

    return f"{grau:,.2f}° Graus equivalem à {radiano:,.2f} Radianos"


def graus_grados (graus: float):

    grados = graus * 200 / 180

    return f"{graus:,.2f}° Graus equivalem à {grados:,.2f}° Grados"


def grados_radiano (grado: float):

    radiano = grado * math.pi / 200

    return f"{grado:,.2f}° Grados equivalem à {radiano:,.2f}° Radianos"


def grados_graus (grado: float):

    graus = grado / 100 * 90

    return f"{grado:,.2f}° Grados equivalem à {graus:,.2f}° Graus"