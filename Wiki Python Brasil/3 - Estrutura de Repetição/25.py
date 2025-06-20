idade_media = 0

contador = 0

while True:

    idade = int(input("Digite a sua idade ou digite 0 para interromper a execução: "))

    if idade == 0:

        break

    else:

        contador += 1

        idade_media += idade

        suficiente = input("Digite sim para calcular a média de idade: ")

        if suficiente == "Sim" or suficiente == "sim":

            idade_media = idade_media / contador

            print(f"A idade média foi {idade_media} anos")

            if idade_media <= 25:

                print("Turma jovem")

            elif idade_media <= 60:

                print("Turma adulta")

            elif idade_media > 60:

                print("Turma idosa")