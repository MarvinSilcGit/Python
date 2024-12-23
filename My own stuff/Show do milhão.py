while True:

    niv = ["", "", "", "", ""]

    div = 0

    ni = 0

    di = 0

    k = 0

    j = 0

    difi = input("Deseja um nível maior de dificuldade? Se sim digite 1, se não, digite 0: ")

    if difi.isdigit()==True:

        while True:

            print()

            pa = [[["esgrima", "boliche", "baseball", "vôlei"], [ "arquiteto", "biólogo", "neorologista", "otorrinolaringologista"], ["foz do iguaçu", "fernando de noronha", "barretos", "aquífero guarani"], ["violino", "sanfona", "atabaque", "flauta"]],
                [["rugby", "polo aquático", "hipismo", "tênis de mesa"], ["assistente social", "professor", "metalúrgico", "pedagogo"], ["gramado", "porto seguro", "caribe", "santa cruz de cabrália"],
                 ["baixolão", "órgão", "ukelele", "zabumba"]]]


            dic=[[["É um esporte olímpico que utiliza uma arma pontiaguda para acertar o corpo do adversário, principalmente a cabeça",
                  "É um esporte olímpico que consiste em derrubar 10 objetos brancos no fim da pista com uma bola de diversas cores",
                  "É um esporte olímpico cujo o objetivo é tomar a base adversária, sendo alinhadas em forma de losango",
                  "É um esporte olímpico que tem como uma das características atletas com média de altura acima de 1,90m"],
                  
                  ["Profissional responsável por projetar ambientes externos e internos, sendo muito prestigiado por isso",
                 "Responsável pelo trabalho com micro organismos, e que cada vez mais é influenciado pela nanotecnologia",
                 "Responsável por analisar o comportamento da massa cinzenta quando estimulada",
                 "Da área da medicina que tem por função tratar e prevenir doenças no sistema respiratório"],
                  
                  ["Fica na divisa do Brasil e Urugaui e é uma das maiores quedas d'guas em volume do mundo",
                     "ilha brasileira paradisíaca, tendo pernambuco como o estado mais próximo",
                     "Muito conhecida por vaquejadas e se encontra no estado de São Paulo",
                     "Local subterrâneo que concentra a maior quantidade de agua doce da América do Sul, sendo situado principalmente no Brasil"],

                  ["Muito utilzado na música clássica e possui uma versão com a marca Estradivários", "Muito utilizado no nordeste Brasileiro, tendo que aperta e soltar para o som sair",
                   "Instrumento de percusão de origem Africana, muito utilizado no axé e camdoblé", "Instrumento de sopro que muitas crianças já tiveram e tem o adjetivo doce"]],
                 
                 [["É um esporte que é semelhante o futebol americano", " Esporte que tem o objetivo de marcar pontos jogando na piscina com água",
                   "Praticado com um equino e um domador", "Praticado com uma raquete em um mesa"],
                  
                  ["Responsável por acolhimento social e familiar para famílias e pessoas carentes", "O profissional que ensina por essência"
                   , "trabalha com materiais pesados, principalmente metais", "reponsável por desenvolver boas práticas escolares"],
                  
                  ["", "Onde os portugues primeiro atracaram no Brasil", "Conhecido pelas águas cristalinas da américa central", "A Alemanha tomou como base para a copa de 2014"],
                  
                  ["Contrabaixo acústico", "Utiizado em igrejas católicas e cristãs americanas",
                   "semelhante ao cavaquinho, mas que não é do Brasil", "Percussão utilizada na músicas nordestinas"]]]
            
            esc = ["Esportes", "Profissões", "Pontos turísticos", "Intrumentos musicais"]

            print("%s!!!" % esc[k])

            print()

            print("Para passar ao próximo nível, resolva uma das %d forcas de cada categoria" % len(pa[div][k]))

            print()

            z = 0

            tudo = 0

            w = []

            x = 0

            certo = 0

            errar = 0

            b = 0

            errado = 3

            letra = 0

            branco = 0

            tudo = len(pa[div][k][j])

            print(dic[div][k][j])

            while True:

                print()

                while z != tudo:

                    if pa[div][k][j][z] == " ":

                        w.append(" ")

                        branco += 1

                    else:

                        w.append("_")

                    z += 1

                p = " ".join(w)

                print("Forca: %s" % p)

                letra = input("Digite uma letra: ").lower()

                print()

                if letra == "" or letra == " ":

                    print("Não é permitido espaço em branco")

                    continue

                elif letra in p:

                    print("Esta letra já foi digitada!")

                    continue

                if letra.isalpha() == True:

                    if len(letra) == 1:

                        while x != tudo:

                            if letra == pa[div][k][j][x]:

                                w[x] = letra

                                certo += 1

                                if certo >= 2:

                                    if difi == "1":

                                        print("Você acertou duas letras agora terá de digitar a palavra inteira!")

                                        print()

                                        acertar = input("Digite a palavra. Se errar, irá para a forca: ")

                                        if acertar.isdigit() == False:

                                            if acertar == pa[div][k][j]:

                                                certo = len(w)-branco

                                                break

                                            else:

                                                errado = 0

                                        else:

                                            print()

                                            print("Digite somente letras!")

                                            print()

                                            continue

                            else:

                                errar += 1

                            if errar == len(w):

                                errado -= 1

                                print("Errado!")

                            x += 1

                    else:

                        print("Digite somente uma letra. Não é permitido mais de uma letra por vez na forca")

                        continue

                    x = 0

                    errar = 0

                else:

                    print("Digite somente letras!")

                    continue

                if errado == 0 or (certo+branco) == len(w):

                    break

            if errado == 0:

                print("Você esgotou suas chances de errar. Enforcado!")

                print()

                print("   O ")

                print("   /\ ")

                print("   || ")

                print("-\   /-")

                print()

                while b != 5:

                    print("  \O/" * 5)

                    print("  \O/" * 5)

                    b += 1

                break

            if (certo+branco) == len(w):

                print()

                print("Você acertou a palavra %s e não foi enforcado!" % pa[div][k][j])

                m = 0

                j += 1

                if j == len(pa[div][k]):

                    if k == len(pa[div][k]):

                        print()

                        k = 0

                        div += 1

                        print("Você passou para o nível %d" % (div+1))

                        continue

                    else:

                        k += 1

                        j = 0

    else:

        print()

        print("Digite somente números!")

        print()

        continue
