def metro_quilometro (metro: float):

    return "%.2f Metros equivalem à %.2f Quilometros" % (metro, metro / 1000)


def metro_centimetro (metro: float):

    return "%.2f Metros equivalem à %.2f Centímetros" % (metro, metro * 100)


def metro_milimetro (metro: float):

    return "%.2f Metros equivalem à %.2f Milímetros" % (metro, metro * 1000)


def metro_micrometro (metro: float):

    return "%.2f Metros equivalem à %.0e Micrômetros" % (metro, metro * 1e+6)


def metro_nanometro (metro: float):

    return "%.2f Metros equivalem à %.0e Nanômetros" % (metro, metro * 1e+9)