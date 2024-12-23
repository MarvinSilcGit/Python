cigarrosDia = int(input("Quantos cigarros você fumou por dia? "))

cigarrosAnos = int(input("Quantos anos você já fomou? "))

cigarrosAnos = 365 * cigarrosAnos

DiasPerdidos = (cigarrosDia * cigarrosAnos * 10) / 60 / 24

print("Você já perdeu %d dias fumando %d cigarros por dia" % (DiasPerdidos, cigarrosDia))
