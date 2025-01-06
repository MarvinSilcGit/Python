def area_quadrado(area: str):

    if not area.isdigit():

        return "Digite somente números"

    else:

        area = int(area)

        area = area * area

        return "A área do quadrado é %d" % area

print(area_quadrado("8"))