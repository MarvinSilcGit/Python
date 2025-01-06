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

print("A cidade com o código %d teve a maior taxa de acidentes com %.2f" % (codigo_cidade_maior_acidente, maior_media_acidentes))

print("A cidade com o código %d teve a menor taxa de acidentes com %.2f" % (codigo_cidade_menor_acidente, menor_media_acidentes))

print("A média de veículos das %d cidades é %.2f" % (contador, media_veiculos))