contador = 1

while contador != 0:

    valor = 1

    contador1 = 0

    contador2 = 0

    media_valor = 0

    while True:

        valor = int(input("Digite um número ou digite 0 para interromper: "))

        contador1 += valor

        contador2 += 1

        if valor == 0 and contador2 == 1:

            print("A iteração parou e não foi realizado nenhum cálculo")

            break

        else:

            if valor == 0:

                contador2 -= 1

                media_valor = contador1 / contador2

                print()

                print("A iteração parou por ter digitado o número %d" % valor)

                print("A média das somas dos números digitados é: %.2f E o valor total da soma é: %d" % (media_valor, contador1))

                break

    print()

    contador = int(input("Digite 0 para interromper a execução: "))

    print()