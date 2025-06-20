numero = int(input("Digite um número para saber a fatorial: "))

resultado_fatorial = numero

for contador in range(numero, 1, -1):

    resultado_fatorial *= contador - 1

print(f"Fatorial de {numero} é {resultado_fatorial}")