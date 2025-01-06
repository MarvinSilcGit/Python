numero_inicial = int(input("Digite o número inicial: "))

numero_final = int(input("Digite o número final: "))

soma = 0

for contador in range(numero_inicial + 1, numero_final):

    print(contador)

    soma += contador

print(soma)