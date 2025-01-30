contador1 = 1

while contador1 != 0:

    numero = float(input("Digite um número para saber a sua raiz aproximada, utilizando o método Newtoniano: "))

    base = 2

    resultado_raiz_quadrada = (base + numero / base) / 2

    resultado_raiz_quadrada **= 2

    while resultado_raiz_quadrada * resultado_raiz_quadrada - numero > 0.001:

        base = resultado_raiz_quadrada

        resultado_raiz_quadrada = (base + numero / base) / 2

    print(f"A raiz aproximada de {numero:,.2f} é {resultado_raiz_quadrada:,.2f}")

    print()

    contador1 = int(input("Digite 0 para interromper a execução: "))

    print()