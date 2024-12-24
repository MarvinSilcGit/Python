cont = "1"

while cont != "0":

    while True:
        # 1 Nesse ponto 1, são definidas as listas dentro de listas. Quatro listas, a primeira é sobre esportes, a segunda sobre empregos, a terceira sobre cidades
        # e a quarta é sobre instrumentos musicais
        # Define-se outra lista para abrigar os valores de cada conjunto de lista com a variável teste

        print("**************************************************************************************")

        pa = [["esgrima", "boliche", "baseball", "vôlei"], ["empreendedor", "design", "neurologista", "otorrinolaringologista"], ["itaquaquecetuba", "pidamonhagaba", "recife", "vitória"], ["violoncelo", "banjo", "acordeon", "xilophone"]]

        print(("Forca 1, Espotes; Forca 2, Profissões; Forca 3, Cidades Brasileiras; Forca 4, Intrumentos musicais" ))

        print("**************************************************************************************")

        num = input("Digite o número de qualquer uma das %d forcas: " % len(pa))

        print()

        teste = ["1", "2", "3", "4"]

        # 1
        # 2 Nesse ponto utiliza-se o método ".isdigit()" para saber se o valor digitado é um número. Se for entra no bloco, se não, recebe um aviso de entrada de dados incorreta

        while True:

            if num.isdigit() == True:

                if num in teste:

                    if num == "1":

                        print()

                        z = 0

                        w = []

                        a = 0

                        x = 0

                        certo1 = 0

                        errar1 = 0

                        b = 0

                        errado1 = 0

                        erro1 = 0

                        certo1 = 0

                        letra1 = 0

                        ent1 = input("Digite de 1 a 4 para escolher um dos esportes e receber suas respectivas dicas ou 0 para voltar ao menu anterior: ")

                        if ent1.isdigit() == True:

                            if ent1 == "0":

                                break

                            elif ent1 == "1":

                                erro1 = len(pa[0][0])

                                if erro1 > 10:

                                    errado1 = 4

                                elif erro1 > 15:

                                    errado1 = 5

                                elif erro1 < 10:

                                    errado1 = 3

                                print()

                                print("É um esporte olímpico que utiliza uma arma pontiaguda para acertar o corpo do adversário, principalmente a cabeça")

                                while True:

                                    print()

                                    while z != len(pa[0][0]):

                                        w.append("_")

                                        z += 1

                                    w = " ".join(w)

                                    print("Forca: %s" % w)

                                    letra1 = input("Digite uma letra: ").lower()

                                    if letra1 in w:

                                        print()

                                        print("Esta letra já foi digitada!")

                                        continue

                                    if letra1.isalpha() == True:

                                        if len(letra1) == 1:

                                            w = w.split()

                                            while x != len(pa[0][0]):

                                                if letra1 == pa[0][0][x]:

                                                    w[x] = letra1

                                                    certo1 += 1

                                                else:

                                                    errar1 += 1

                                                if errar1 == len(w):

                                                    errado1 -= 1

                                                    print()

                                                    print("Errado!")

                                                x += 1

                                        else:

                                            print()

                                            print("Digite somente uma letra. Não é permitido mais de uma letra por vez na forca")

                                            continue

                                        x = 0


                                        errar1 = 0

                                    else:

                                        print()

                                        print("Digite somente letras!")

                                        continue

                                    if errado1 == 0 or certo1 == len(w):

                                        break

                            elif ent1 == "2":

                                erro1 = len(pa[0][1])

                                if erro1 > 10:

                                    errado1 = 4

                                elif erro1 > 15:

                                    errado1 = 5

                                elif erro1 < 10:

                                    errado1 = 3

                                print()

                                print("É um esporte olímpico que consiste em derrubar 10 objetos brancos no fim da pista com uma bola de diversas cores, com o menor número possível de jogadas")

                                while True:

                                    print()

                                    while z != len(pa[0][1]):

                                        w.append("_")

                                        z += 1

                                    w = " ".join(w)

                                    print("Forca %s" % w)

                                    letra1 = input("Digite um letra: ").lower()

                                    if letra1 in w:

                                        print()

                                        print("Esta letra já foi digitada!")

                                        continue

                                    if letra1.isalpha() == True:

                                        if len(letra1) == 1:

                                            w = w.split()

                                            while x != len(pa[0][1]):

                                                if letra1 == pa[0][1][x]:

                                                    w[x] = letra1

                                                    certo1 += 1

                                                else:

                                                    errar1 += 1

                                                if errar1 == len(w):

                                                    errado1 -= 1

                                                    print()

                                                    print("Errado!")

                                                x += 1

                                        else:

                                            print()

                                            print("Digite somente uma letra. Não é permitido mais de uma letra por vez na forca")

                                            continue

                                        x = 0

                                        errar1 = 0

                                    else:

                                        print()

                                        print("Digite somente letras")

                                        continue

                                    if errado1 == 0 or certo1 == len(w):

                                        break

                            elif ent1 == "3":

                                erro1 = len(pa[0][2])

                                if erro1 > 10:

                                    errado1 = 4

                                elif erro1 > 15:

                                    errado1 = 5

                                elif erro1 < 10:

                                    errado1 = 3

                                print()

                                print("É um esporte olímpico cujo o objetivo é tomar a base adversária, percorrendo as base, que são alinhadas em forma de losango")

                                while True:

                                    print()

                                    while z != len(pa[0][2]):

                                        w.append("_")

                                        z += 1

                                    w = " ".join(w)

                                    print("Forca: %s" % w)

                                    letra1 = input("Digite uma letra: ").lower()

                                    if letra1 in w:

                                        print()

                                        print("Esta letra já foi digitada!")

                                        continue

                                    if letra1.isalpha() == True:

                                        if len(letra1) == 1:

                                            w = w.split()

                                            while x != len(pa[0][2]):

                                                if letra1 == pa[0][2][x]:

                                                    w[x] = letra1

                                                    certo1 += 1

                                                else:

                                                    errar1 += 1

                                                if errar1 == len(w):

                                                    errado1 -= 1

                                                    print()

                                                    print("Errado!")

                                                x += 1

                                        else:

                                            print()

                                            print("Digite somente um letra. Não é permitido mais de uma letra por vez na forca")

                                            continue

                                        x = 0

                                        errar1 = 0

                                    else:

                                        print()

                                        print("Digite somente letras!")

                                        continue

                                    if errado1 == 0 or certo1 == len(w):

                                        break

                            elif ent1 == "4":

                                erro1 = len(pa[0][3])

                                if erro1 > 10:

                                    errado1 = 4

                                elif erro1 > 15:

                                    errado1 = 5

                                elif erro1 < 10:

                                    errado1 = 3

                                print()

                                print("É um esporte olímpico que tem como uma das características atletas com média de altura acima de 1,90m e que possui uma rede dividindo os times")

                                while True:

                                    print()

                                    while z != len(pa[0][3]):

                                        w.append("_")

                                        z += 1

                                    w =" ".join(w)

                                    print("Forca: %s" % w)

                                    letra1 = input("Digite uma letra: ").lower()

                                    if letra1 in w:

                                        print()

                                        print("Esta letra já foi digitada!")

                                        continue

                                    if letra1.isalpha() == True:

                                        if len(letra1) == 1:

                                            w = w.split()

                                            while x != len(pa[0][3]):

                                                if letra1 == pa[0][3][x]:

                                                    w[x] = letra1

                                                    certo1 += 1

                                                else:

                                                    errar1 += 1

                                                if errar1 == len(w):

                                                    errado1 -= 1

                                                    print()

                                                    print("Errado!")

                                                x += 1

                                        else:

                                            print()

                                            print("Digite somente uma letra. Não é permitido mais de uma letra por vez na forca")

                                            continue

                                        x = 0

                                        errar1 = 0

                                    else:

                                        print()

                                        print("Digite somente letras!")

                                        continue

                                    if errado1 == 0 or certo1 == len(w):

                                        break

                            elif ent1 != "0" and ent1 != "1" and ent1 != "2" and ent1 != " 3" and ent1 != "4":

                                print()

                                print("Digite apenas entre 0 e 4!")

                                continue

                            if errado1 == 0:

                                print()

                                print("Você esgotou suas chances de errar. Enforcado!")

                                print()

                                if errado1 < 3:

                                    print("   O ")

                                if errado1 < 2:

                                    print("   /\ ")

                                if errado1 < 1:

                                    print("   || ")

                                    print("-\   /-")

                                    print()

                                    while b != 5:

                                        print("  \O/"*5)

                                        print("  \O/"*5)

                                        b += 1

                            print()

                            if certo1 == len(w) and ent1 == "1":

                                print("Você acertou a palavra %s e não foi enforcado!"%pa[0][0])

                            elif certo1 == len(w) and ent1 == "2":

                                print("Você acertou a palavra %s e não foi enforcado!"%pa[0][1])

                            elif certo1 == len(w) and ent1 == "3":

                                print("Você acertou a palavra %s e não foi enforcado!"%pa[0][2])

                            elif certo1 == len(w) and ent1 == "4":

                                print("Você acertou a palavra %s e não foi enforcado!"%pa[0][3])

                        else:

                            print()

                            print("Digite somente números!")

                            continue

                    elif num == "2":

                        print("2")

                    elif num == "3":

                        print("3")

                    elif num == "4":

                        print("4")

                else:

                    print("Digite somente os números das forcas!")

                    break

            else:

                print("Digite somente números!")

                break

    # 2 Aqui termina a verificação de entrada de dados

    print()

    cont = input("Digite 0 para interromper a execução: ")

    if cont.isdigit() == True:

        break

    else:

        print("Digite apenas números!")

        continue
