numeroInicial = int(input("Digite o número inicial: "))

numeroFinal = int(input("Digite o número final: "))

soma = 0

for contador in range(numeroInicial + 1, numeroFinal):

    print(contador)

    soma += contador

print(soma)