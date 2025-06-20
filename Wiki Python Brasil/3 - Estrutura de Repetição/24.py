contador = 1

contador2 = 0

media_notas = 0


while contador != 0:

    notas = float(input("Digite uma nota ou digite 0 para interromper a execução: "))

    if notas == 0:

        contador = notas

    else:

        media_notas += notas

        contador2 += 1


media_notas = media_notas / contador2

print(f"A média das notas foi {media_notas:.2f}")