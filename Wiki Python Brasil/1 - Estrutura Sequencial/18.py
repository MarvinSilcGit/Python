tamanho_arquivo = float(input("Digite o tamanho do arquivo em Megabytes: "))

if tamanho_arquivo < 1:

    print("Valor inválido!")

velecidade_link = float(input("Digite a velocidade de sua conexão em megabits: "))

tempo_download = (tamanho_arquivo / (velecidade_link / 8))

if tempo_download >= 60:

    tempo_download = tempo_download / 60

    print(f"O tempo de Download será de no mínimo {tempo_download:.1f} minutos")

else:

    print(f"O tempo de Download será de no mínimo {tempo_download:.1f} segundos")