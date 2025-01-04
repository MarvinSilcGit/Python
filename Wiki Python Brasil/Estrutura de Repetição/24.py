contador = 1

contador2 = 0

mediaNotas = 0

while contador != 0:

    notas = float(input("Digite uma nota ou digite 0 para interromper a execução: "))

    if notas == 0:

        contador = notas

    else:

        mediaNotas += notas

        contador2 += 1

mediaNotas = mediaNotas / contador2

print("A média das notas foi %.2f" % mediaNotas)