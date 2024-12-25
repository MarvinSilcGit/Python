cigarrosDia = int(input("Quantos cigarros você fumou por dia? "))

cigarrosAnos = int(input("Por quantos anos você fomou? "))

cigarrosTotal = 365 * cigarrosAnos * cigarrosDia

diasPerdidos = cigarrosTotal * 10 / 60 / 24

print("Você já perdeu %d dias fumando %d cigarro(s) por dia, por %d anos" % (diasPerdidos, cigarrosDia, cigarrosAnos))