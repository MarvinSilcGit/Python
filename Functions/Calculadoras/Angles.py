import math

def radiano_graus (radiano: float):
    """Função responsável por converter Radianos em Graus. Fórmula: radiano * 180 / 3,14"""
    try:

        graus = radiano * 180 / math.pi

    except TypeError:

        return 'Somente números são permitidos'

    else:

        return graus


def radiano_grados (radiano: float):
    """Função responsável por converter Radianos em Grados. Fórmula: radiano * 200 / 3,14"""
    try:

        grados = radiano * 200 / math.pi

    except TypeError:

        return 'Somente números são permitidos'

    else:

        return grados


def graus_radiano (grau: float):
    """Função responsável por converter Graus em Radianos. Fórmula: graus * 3,14 / 180"""
    try:

        radiano = grau * math.pi / 180

    except TypeError:

        return 'Somente números são permitidos'

    else:

        return radiano


def graus_grados (graus: float):
    """Função responsável por converter Graus em Grados. Fórmula: graus * 200 / 180"""
    try:

        grados = graus * 200 / 180

    except TypeError:

        return 'Somente números são permitidos'

    else:

        return grados


def grados_radiano (grado: float):
    """Função responsável por converter Grados em Radianos. Fórmula: graus * 3,14 / 200"""
    try:

        radiano = grado * math.pi / 200

    except TypeError:

        return 'Somente números são permitidos'

    else:

        return radiano


def grados_graus (grado: float):
    """Função responsável por converter Grados em Graus. Fórmula: grados / 100 * 90"""
    try:

        graus = grado / 100 * 90

    except TypeError:

        return 'Somente números são permitidos'

    else:

        return graus