confirmacao = 2

numero = int(input("Digite um número inteiro para saber se ele é primo ou não: "))

if numero == 0 or numero == 1:

    print("Esse número é inválido")

if numero == 2 or numero == 3:

    print("%d é um número primo" % numero)

else:

    for contador in range(confirmacao, numero + 1):

        if numero % contador != 0:

            confirmacao += 1

    if confirmacao == numero:

        print("%d é um número primo" % numero)

    else:

       print("O número %d não é primo, pois ele é divisível por: " % numero, end="")

       for contador in range(1, numero + 1):

           if numero % contador == 0:

               if numero - contador == 0:

                   print(contador, end=" ")

               else:

                    print(contador, end=", ")