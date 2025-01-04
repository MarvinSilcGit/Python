idadeMedia = 0

contador = 0

while True:

    idade = int(input("Digite a sua idade ou digite 0 para interromper a execução: "))

    if idade == 0:

        break

    else:

        contador += 1

        idadeMedia += idade

        suficiente = input("Digite sim para calcular a média de idade: ")

        if suficiente == "Sim" or suficiente == "sim":

            idadeMedia = idadeMedia / contador

            print("A idade média foi %.2f anos" % idadeMedia)

            if idadeMedia <= 25:

                print("Turma jovem")

            elif idadeMedia <= 60:

                print("Turma adulta")

            elif idadeMedia > 60:

                print("Turma idosa")