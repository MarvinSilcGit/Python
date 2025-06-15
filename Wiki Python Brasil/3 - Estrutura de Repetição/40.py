maior_media_acidentes = 0

menor_media_acidentes = 0

media_veiculos = 0

codigo_cidade_menor_acidente = 0

codigo_cidade_maior_acidente = 0

contador = 0

while contador != 5:

    codigo = int(input("Digite o código da cidade: "))

    numero_veiculos = int(input("Digite o número de veículo na cidade: "))

    numero_acidentes = int(input("Digite o número de acidentes no ano: "))

    if menor_media_acidentes == 0:

        menor_media_acidentes = numero_acidentes / numero_veiculos * 100

        codigo_cidade_menor_acidente = codigo

    if maior_media_acidentes < numero_acidentes / numero_veiculos * 100:

        maior_media_acidentes = numero_acidentes / numero_veiculos * 100

        codigo_cidade_maior_acidente = codigo

    if menor_media_acidentes > numero_acidentes / numero_veiculos * 100:

        menor_media_acidentes = numero_acidentes / numero_veiculos * 100

        codigo_cidade_menor_acidente = codigo

    media_veiculos += numero_veiculos

    contador += 1

media_veiculos = media_veiculos / contador

print(f"A cidade com o código {codigo_cidade_maior_acidente} teve a maior taxa de acidentes com {maior_media_acidentes:.2f}")

print(f"A cidade com o código {codigo_cidade_menor_acidente} teve a menor taxa de acidentes com {menor_media_acidentes:.2f}")

print(f"A média de veículos das {contador} cidades é {media_veiculos:.2f}")