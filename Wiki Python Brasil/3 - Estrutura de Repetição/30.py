preco = float(input("Digite o preço da unidade do Pão: "))

for contador in range(1, 51):

    print(f"{contador} - R$ {preco * contador:.2f}")