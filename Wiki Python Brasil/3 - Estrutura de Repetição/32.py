numero = int(input("Fatorial de: "))

resultado_fatorial = numero

print("%d! =" % numero, end=" ")

for contador in range(numero, 0, -1):

    if contador == 1:

        print("%d" % contador, end=" = ")

        break

    else:

        resultado_fatorial *= contador - 1

        print("%d" % contador, end=" x ")

print(resultado_fatorial)