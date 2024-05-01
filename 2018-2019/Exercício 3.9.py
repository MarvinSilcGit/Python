dias = int(input("DIGITE A QUANTIDADE DE DIAS: "))

horas = int(input("DIGITE A QUANTIDADE DE HORAS: "))

minutos = int(input("DIGITE A QUANTIDADE DE MINUTOS: "))

segundos = int(input("DIGITE A QUANTIDADE DE SEGUNDOS: "))

horas = dias*24+horas

minutos = horas*60+minutos

segundos = minutos*60+segundos

print("%d dias dura ao equivalente à %d segundos" % (dias, segundos))

print(minutos)
