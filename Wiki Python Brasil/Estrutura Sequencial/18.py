contador = 1

while contador != 0:

    tamanhoArquivo = float(input("Digite o tamanho do arquivo em Megabytes: "))

    if tamanhoArquivo < 1:

        print("Valor inválido!")

        continue

    velecidadeLink = float(input("Digite a velocidade de sua conexão em megabits: "))

    tempoDownload = (tamanhoArquivo / (velecidadeLink / 8))

    if tempoDownload >= 60:

        tempoDownload = tempoDownload / 60

        print("O tempo de Download será de no mínimo %.1f minutos e %d segundos" % (tempoDownload, tempoDownload))

    else:

        print("O tempo de Download será de no mínimo %.1f segundos" % tempoDownload)

    print()

    contador = int(input("Digite 0 para interromper a execução: "))

    print()