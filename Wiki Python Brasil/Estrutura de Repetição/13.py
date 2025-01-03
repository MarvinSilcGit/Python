base = int(input("Digite o número base: "))

expoente = int(input("Digite o número expoente: "))

resultado = base

for contador in range(expoente - 1):

    resultado *= base

print(resultado)