valor = 1

contador1 = 0

contador2 = 0

mediaValor = 0

while True:

    valor = int(input("Digite um número: "))

    if valor == 0 and contador2 == 0:

        print("Não foi feito nenhum cálculo")

        print()

        continue

    else:

        contador1 += valor

        contador2 += 1

        zero = input("Digite zero para finalizar: ")

        if zero == "0":

            mediaValor = contador1 / contador2

            print("A iteração parou por ter digitado o número 0")

            print("A média das somas dos números digitados é: %d. E o valor total da soma é: %d" % (mediaValor, contador1))

            contador2 = 0

            valor = 0

            contador1 = 0