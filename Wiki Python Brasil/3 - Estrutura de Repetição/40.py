maior_media_acidentes = 0

menor_media_acidentes = 0

media_veiculos = 0

codigo_cidade_menos_acidentes = 0

codigo_cidade_mais_acidentes = 0

contador = 0

for contador in range(5):

    codigo = int(input("Digite o código da cidade: "))

    numero_veiculos = int(input("Digite o número de veículo na cidade: "))

    numero_acidentes = int(input("Digite o número de acidentes no ano: "))

    if menor_media_acidentes == 0:

        menor_media_acidentes = numero_acidentes / numero_veiculos * 100

        codigo_cidade_menos_acidentes = codigo

    if maior_media_acidentes < numero_acidentes / numero_veiculos * 100:

        maior_media_acidentes = numero_acidentes / numero_veiculos * 100

        codigo_cidade_mais_acidentes = codigo

    if menor_media_acidentes > numero_acidentes / numero_veiculos * 100:

        menor_media_acidentes = numero_acidentes / numero_veiculos * 100

        codigo_cidade_menos_acidentes = codigo

    media_veiculos += numero_veiculos

print(f"A cidade com o código {codigo_cidade_mais_acidentes} teve a maior taxa de acidentes com {maior_media_acidentes:.2f}")

print(f"A cidade com o código {codigo_cidade_menos_acidentes} teve a menor taxa de acidentes com {menor_media_acidentes:.2f}")

print(f"A média de veículos das {contador+1} cidades é {media_veiculos/contador+1:.2f}")