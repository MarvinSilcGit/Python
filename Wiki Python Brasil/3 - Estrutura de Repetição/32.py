numero = int(input("Fatorial de: "))

resultado_fatorial = numero

print(f"{numero}! =", end=" ")

for contador in range(numero, 0, -1):

    if contador == 1:

        print(f"{contador}", end=" = ")

    else:

        resultado_fatorial *= contador - 1

        print(f"{contador}", end=" x ")

print(resultado_fatorial)