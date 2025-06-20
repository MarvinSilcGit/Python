confirmacao = 2

numero = int(input("Digite um número inteiro para saber se ele é primo ou não: "))

if numero <= 1:

    print("Esse número é inválido")


else:

    for contador in range(confirmacao, numero + 1):

        if numero % contador != 0:

            confirmacao += 1

    print(f"O número {numero} é um número primo") if confirmacao == numero else print(f"O número {numero} não é primo, pois ele é divisível por: ", end="")

    for contador in range(1, numero + 1):

       if numero % contador == 0:

           print(contador, end=" ") if numero - contador == 0 else print(contador, end=", ")