KilometrosPercorridos = float(input("Quantos kilômetros foram percorridos com o carro? "))

diasAlugado = int(input("Por quantos dias o carro foi alugado? "))

diariaAluguel = 60*diasAlugado

custoKilometro = 0.15*KilometrosPercorridos

custoAluguel = diariaAluguel+custoKilometro

print("O custo total do aluguel foi de %2.f R$, por um carro que foi alugado por %d dias e com uma kilometragem de %.2f kilômetros" % (custoAluguel, diasAlugado, KilometrosPercorridos))
