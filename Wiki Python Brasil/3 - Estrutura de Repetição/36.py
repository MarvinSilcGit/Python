tabuada = int(input("Montar tabuada de: "))

inicio_tabuada = int(input("Começar por: "))

fim_tabudada = int(input("Terminar em: "))

if fim_tabudada <= inicio_tabuada:

    print("O fim não pode ser menor ou igual ao início da tabuada")

else:

    print()

    print(f"Vou montar a tabuada de {tabuada}, começando por {inicio_tabuada} e terrminando em {fim_tabudada}:")

    for contador in range(inicio_tabuada, fim_tabudada + 1):

        print(f"{tabuada} x {contador} = {tabuada * contador}")