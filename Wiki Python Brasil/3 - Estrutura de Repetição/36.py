tabuada = int(input("Montar tabuada de: "))

inicio_tabuada = int(input("Começar por: "))

fim_tabudada = int(input("Terminar em: "))

if fim_tabudada <= inicio_tabuada:

    print("O fim não pode ser menor ou igual ao início da tabuada")

else:

    print()

    print("Vou montar a tabuada de %d, começando por %d e terrminando em %d:" % (tabuada, inicio_tabuada, fim_tabudada))

    for contador in range(inicio_tabuada, fim_tabudada + 1):

        print("%d x %d = %d " % (tabuada, contador, tabuada * contador))