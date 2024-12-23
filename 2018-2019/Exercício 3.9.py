dias = int(input("Digite a quantidade de dia: "))

horas = int(input("Digite a quantidade de horas: "))

minutos = int(input("Digite a quantidade de minutos: "))

segundos = int(input("Digite a quantidade de segundos: "))

horas = dias * 24 + horas

minutos = horas * 60 + minutos

segundos = minutos * 60 + segundos

print("%d dia(s) dura ao equivalente à %d segundos" % (dias, segundos))