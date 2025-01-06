contador = 1

while contador != 0:

    numero = int(input("Digite um número para saber a fatorial: "))

    if numero > 16:

        print("Somente número menores que 16")

        continue

    resultado_fatorial = numero

    for contador in range(numero, 1, -1):

        resultado_fatorial *= contador - 1

    print("Fatorial de %d é %d" % (numero, resultado_fatorial))

    contador = int(input("Digite 0 para interromper a execução: "))