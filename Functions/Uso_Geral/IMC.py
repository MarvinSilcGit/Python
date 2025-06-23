def calculo_imc (peso: float, altura: float):
    """Função responável por calcular o IMC de uma pessoa."""
    return f"{peso / altura ** 2:.1f}"