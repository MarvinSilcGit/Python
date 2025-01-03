contador = 1

while contador != 0:

    nota = int(input("Digite uma nota entre 1 e 10: "))

    if nota >= 1 and nota <= 10:

        print(nota)

    else:

        print("Nota inválida")

        continue

    contador = int(input("Digite 0 para finalizar o programa: "))