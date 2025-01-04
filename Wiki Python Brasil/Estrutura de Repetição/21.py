confirmacao = 2

numero = int(input("Digite um número inteiro para saber se ele é primo ou não: "))

contador = 5

if numero == 0 or numero == 1:

    print("Esse número é inválido")

if numero == 2 or numero == 3:

    print("%d é um número primo" % numero)

else:

    for contador in range(2, numero + 1):

        if numero % contador != 0:

            confirmacao += 1

    if confirmacao == numero:

        print("%d é um número primo" % numero)

    else:

       print("%d não é um número primo" % numero)