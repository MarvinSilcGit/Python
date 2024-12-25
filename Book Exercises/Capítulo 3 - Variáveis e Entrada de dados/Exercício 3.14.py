kilometrosPercorridos = float(input("Quantos kilômetros foram percorridos com o carro? "))

diasAlugados = int(input("Por quantos dias o carro foi alugado? "))

diariaAluguel = 60 * diasAlugados

custoKilometro = 0.15 * kilometrosPercorridos

custoTotalAluguel = diariaAluguel + custoKilometro

print("O custo total do aluguel foi de R$ %.2f, por um carro que foi alugado por %d dias e com %.1f kilômetros percorridos" % (custoTotalAluguel, diasAlugados, kilometrosPercorridos))
