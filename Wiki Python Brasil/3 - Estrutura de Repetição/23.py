contador = 1

confirmacao = 2

divisoes = 0

contagem_primos = 0

while contador != 0:

    numero_inicial = int(input("Digite o número inicial: "))

    numero_final = int(input("Digite o número final: "))

    numero_primario = numero_inicial

    if numero_inicial < 2 or numero_final <= numero_inicial:

        print("Combinação inválida!")

        continue

    else:

        for contador2 in range(numero_inicial, numero_final + 1):

            for contador3 in range(confirmacao, numero_inicial + 1):

                if numero_inicial % contador3 != 0:

                    confirmacao += 1

                divisoes +=1

            if confirmacao == numero_inicial:

                print(f"{numero_inicial} é um número primo e foram feitas {divisoes} divisões")

                contagem_primos += 1

            else:

                print(f"{numero_inicial} não é um número primo")

            confirmacao = 2

            contador3 = 2

            numero_inicial += 1

            divisoes = 0

    print(f"Existem ao todo {contagem_primos} números primos entre {numero_primario} e {numero_final}")
    print()

    contador = int(input("Digite 0 para interromper a execução: "))

    print()