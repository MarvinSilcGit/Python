distancia = float(input("Qual a distância que irá percorrer? "))

if distancia <= 200:

    passagem = distancia * 0.50

    print("Com uma distância inferior à 200 kilômetros o passageiro irá pagar R$ %.2f pela distância de %.2f kilômetros percorridos"%(passagem, distancia))

else:

    passagem = distancia * 0.45

    print("Com uma distância superior à 200 kilômetros o passageiro irá pagar R$ %.2f pela distância de %.2f kilômetros percorridos"%(passagem, distancia))