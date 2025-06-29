from Alfabeto import listagem_alfabeto

dict_palavras_dicas = {"esgrima": "É um esporte olímpico que utiliza uma lâmina pontiaguda para acertar o corpo do adversário, principalmente a cabeça",
                       "boliche": "É um esporte olímpico que consiste em derrubar 10 objetos brancos no fim da pista com uma bola de diversas cores",
                       "baseball": "É um esporte olímpico cujo o objetivo é tomar a base adversária, sendo alinhadas em forma de losango",
                       "vôlei": "É um esporte olímpico que tem como uma das características atletas com média de altura acima de 1,90m",
                       "arquiteto": "Profissional responsável por projetar ambientes externos e internos, sendo muito prestigiado por isso",
                       "biólogo": "Responsável pelo trabalho com micro organismos, e que cada vez mais é influenciado pela nanotecnologia",
                       "neurologista": "Responsável por analisar o comportamento da massa cinzenta quando estimulada",
                       "otorrinolaringologista": "Formado da área da medicina que tem por função tratar e prevenir doenças no sistema respiratório e auditivo",
                       "foz do iguaçu": "Fica na divisa do Brasil e Uruguai e é uma das maiores quedas d'guas em volume do mundo",
                       "fernando de noronha": "ilha brasileira paradisíaca, tendo pernambuco como o estado mais próximo",
                       "barretos": "Cidade muito conhecida por vaquejadas e se encontra no estado de São Paulo" ,
                       "aquífero guarani": "Local subterrâneo que concentra a maior quantidade de agua doce da América do Sul, sendo situado principalmente no Brasil",
                       "violino": "Muito utilizado na música clássica e possui uma versão com a marca Estradivários",
                       "sanfona": "Muito utilizado no nordeste Brasileiro, tendo que aperta e soltar para o som sair",
                       "atabaque": "Instrumento de percussão de origem Africana, muito utilizado no axé e candomblé" ,
                       "flauta": "Instrumento de sopro que muitas crianças já tiveram e tem o adjetivo doce" ,
                       "rugby": "É um esporte que é semelhante ao futebol americano",
                       "polo aquático": "Esporte que tem o objetivo de marcar pontos jogando na piscina com água",
                       "hipismo": "Praticado com um equino e um domador",
                       "tênis de mesa": "Praticado com uma raquete em um mesa",
                       "assistente social": "Responsável por acolhimento social e familiar para famílias e pessoas carentes",
                       "profissional": "O profissional que ensina por essência",
                       "metalúrgico": "trabalha com materiais pesados, principalmente metais",
                       "pedagogo": "responsável por desenvolver boas práticas escolares",
                       "gramado": "Cidadezinha turística no sul do Brasil",
                       "porto seguro": "Onde os portugueses primeiro atracaram no Brasil",
                       "caribe": "Região conhecida pelas águas cristalinas da américa central",
                       "santa cruz de cabrália": "A Alemanha tomou como base para a copa de 2014",
                       "baixolão": "Contrabaixo acústico",
                       "órgão": "Utilizado em igrejas católicas e cristãs americanas",
                       "ukelele": "instrumento semelhante ao cavaquinho, popular do havaí",
                       "zabumba": "Percussão utilizada na músicas nordestinas"}

while True:

    contagem_letras_digitadas = []

    while True:

        letra_digitada = input("Digite uma letra: ")

        print()

        if listagem_alfabeto(letra_digitada):

            if letra_digitada in contagem_letras_digitadas:

                print("Esta letra já foi digitada!")

            else:

                contagem_letras_digitadas.append(letra_digitada)

        else:

            print('Letra inválida')