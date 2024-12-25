distancia = int(input("Qual a distância que irá percorrer? "))

if distancia <= 200:

    passagem = distancia*0.50

    print("Com uma distância inferior à 200 kilômetros o passageiro irá pagar %.2f R$ pela distância de %d kilômetros percorridos"%(passagem, distancia))

else:

    if distancia > 200:

        passagem = distancia*0.45

        print("Com uma distância superior à 200 kilômetros o passageiro irá pagar %.2f R$ pela distância de %d kilômetros percorridos"%(passagem, distancia))
