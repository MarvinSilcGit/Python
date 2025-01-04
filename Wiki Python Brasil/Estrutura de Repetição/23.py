confirmacao = 2

numero = int(input("Digite o número inicial: "))

numero2 = int(input("Digite o número final: "))

for contador in range(numero, numero2 + 1):

    if numero == 0 or numero == 1:

        print("Esse número é inválido")

        continue

    else:

        for contador2 in range(confirmacao, numero + 1):

            if numero % contador2 != 0:

                confirmacao += 1

        if confirmacao == numero:

            print("%d é um número primo" % numero)

        else:

            print("%d não é um número primo" % numero)

        confirmacao = 2

        contador2 = 2

        numero +=1