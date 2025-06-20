contador = 1

contador2 = 1

mediaAlunos = 0

while contador != 0:

    quantidadeTurmas = int(input("Digite a quantidade de turmas: "))

    if quantidadeTurmas < 1:

        print("Digite um valor maior que 0")

        continue

    while quantidadeTurmas - contador2 + 1 > 0:

        quantidadeAlunos = int(input(f"Digite a quantidade de alunos na turma {contador2}:"))

        if quantidadeAlunos > 40 or quantidadeAlunos < 1:

            print("Quantidade de alunos inválida")

            continue

        else:

            mediaAlunos += quantidadeAlunos

            contador2 += 1

    mediaAlunos = mediaAlunos / quantidadeTurmas

    print(f"A média de alunos por turma é {mediaAlunos:.2f}")

    print()

    contador = int(input("Digite 0 para interromper a execução: "))

    print()