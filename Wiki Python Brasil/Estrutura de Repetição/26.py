contador = 1

candidato1 = 0

candidato2 = 0

candidato3 = 0

while contador != 0:

    numeroEleitores = int(input("Número total de eleitores: "))

    for contador2 in range(1, numeroEleitores + 1):

        print("Qual o voto do eleitor %d ?" % contador2)

        print("Candidato 1 - 23\nCandidato 2 - 15\nCandidato 3 - 18")

        voto = int(input(""))

        if voto == 23:

            candidato1 += 1

        elif voto == 15:

            candidato2 += 1

        elif voto == 18:

            candidato3 += 1

        else:

            print("Candidato inexistente. Voto foi nulo")

    if candidato1 > candidato2 and candidato1 > candidato3:

        print("O vencedor foi o canditado 1 com %d votos" % candidato1)

    elif candidato2 > candidato1 and candidato2 > candidato3:

        print("O vencedor foi o canditado 2 com %d votos" % candidato2)

    elif candidato3 > candidato2 and candidato3 > candidato1:

        print("O vencedor foi o canditado 3 com %d votos" % candidato3)