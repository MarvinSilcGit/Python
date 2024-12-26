contador = 1

while contador != 0:

    pontos = 0

    for questao in range (1, 4):

        resposta = input("Digite a reposta da questao %d : " % questao)

        if questao == 1 and resposta == "b" or resposta == "B":

            pontos = pontos + 1

        elif questao == 2 and resposta == "a" or resposta == "A":

            pontos = pontos + 1

        elif questao == 3 and resposta == "d" or resposta == "D":

            pontos = pontos + 1

        questao += 1

        print("O aluno fez %d pontos(s)" % pontos)

    print()

    contador = int(input("Digite 0 para interromper a execução: "))

    print()