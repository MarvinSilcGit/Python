contador = 1

candidato1 = 0

candidato2 = 0

candidato3 = 0

while contador != 0:

    numero_eleitores = int(input("Número total de eleitores: "))

    for contador2 in range(1, numero_eleitores + 1):

        print(f"Qual o voto do eleitor {contador2} ?")

        voto = int(input("Candidato 1 - 23\nCandidato 2 - 15\nCandidato 3 - 18\n"))

        if voto == 23:

            candidato1 += 1

        elif voto == 15:

            candidato2 += 1

        elif voto == 18:

            candidato3 += 1

        else:

            print("Candidato inexistente. Voto foi nulo")

    if candidato1 > candidato2 and candidato1 > candidato3:

        print(f"O vencedor foi o candidato 1 com {candidato1} votos")

    elif candidato2 > candidato1 and candidato2 > candidato3:

        print(f"O vencedor foi o candidato 2 com {candidato2} votos")

    elif candidato3 > candidato2 and candidato3 > candidato1:

        print(f"O vencedor foi o candidato 3 com {candidato3} votos")