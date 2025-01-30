contador1 = 1

while contador1 != 0:

    valor_inicial = int(input("Digite o valor inicial: "))

    if valor_inicial != 1:

        print("Número incorreto")

        continue

    else:

        valor_final = int(input("Digite o valor final: "))

        while valor_inicial < valor_final:

            print(valor_inicial)

            valor_inicial += 2

        print()

        contador1 = int(input("Digite 0 para interromper a execução: "))