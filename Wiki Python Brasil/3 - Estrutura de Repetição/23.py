contador = 1

confirmacao = 2

divisoes = 0

while contador != 0:

    numero = int(input("Digite o número inicial: "))

    if numero == 0 or numero == 1:

        print("Esse número é inválido")

        continue

    else:

        numero2 = int(input("Digite o número final: "))

        if numero2 <= numero:

            print("Número final não pode ser menor ou igual ao número inicial")

            continue

        else:

            for contador2 in range(numero, numero2 + 1):

                for contador3 in range(confirmacao, numero + 1):

                    if numero % contador3 != 0:

                        confirmacao += 1

                    divisoes +=1

                if confirmacao == numero:

                    print("%d é um número primo e foram feitas %d divisões" % (numero, divisoes))

                else:

                    print("%d não é um número primo" % numero)

                confirmacao = 2

                contador3 = 2

                numero += 1

                divisoes = 0

    print()

    contador = int(input("Digite 0 para interromper a execução: "))

    print()