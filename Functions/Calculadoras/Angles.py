import math

def radiano_graus (radiano: float):

    graus = radiano * 180 / math.pi

    return f"{graus:,.2f}"


def radiano_grados (radiano: float):

    grados = radiano * 200 / math.pi

    return f"{grados:,.2f}°"


def graus_radiano (grau: float):

    radiano = grau * math.pi / 180

    return f"{radiano:,.2f}"


def graus_grados (graus: float):

    grados = graus * 200 / 180

    return f"{grados:,.2f}"


def grados_radiano (grado: float):

    radiano = grado * math.pi / 200

    return f"{radiano:,.2f}"


def grados_graus (grado: float):

    graus = grado / 100 * 90

    return f"{graus:,.2f}"