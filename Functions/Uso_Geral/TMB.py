def calculo_tmb (peso: float, altura: float, idade: int, genero: str):
    """Função responsável por calcular a taxa metabólica basal de uma pessoa."""
    lista_generos = ["Masculino", "masculino", "Feminino", "feminino"]

    if genero not in lista_generos:

        return "Gênero inválido"

    else:

        if genero == "Masculino" or genero == "masculino":

            taxa_metabolica_basal = (10 * peso) + (6.25 * altura) - (5 * idade) + 5

            return taxa_metabolica_basal

        elif genero == "Feminino" or genero == "feminino":

            taxa_metabolica_basal = (10 * peso) + (6.25 * altura) - (5 * idade) - 161

            return taxa_metabolica_basal