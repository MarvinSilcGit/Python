def fahrenheit_celsius (temperatura: float):

    temperatura_celsius = (temperatura - 32) * 5 / 9

    return f"{temperatura_celsius:,.1f}"

def fahrenheit_kelvin (temperatura: float):

    temperatura_kelvin = (temperatura - 32) * 5 / 9 + 273.15

    return f"{temperatura_kelvin:,.1f}"


def fahrenheit_rankine (temperatura: float):

    temperatura_rankine = temperatura + 459.67

    return f"{temperatura_rankine:,.1f}"


def celsius_fahrenheit (temperatura: float):

    temperatura_fahrenheit = (temperatura * 5 / 9) + 32

    return f"{temperatura_fahrenheit:,.1f}"


def celsius_kelvin (temperatura: float):

    temperatura_kelvin = temperatura + 273.15

    return f"{temperatura_kelvin:,.1f}"


def celsius_rankine (temperatura: float):

    temperatura_rankine = (temperatura - 491.67) * 5 / 9

    return f"{temperatura_rankine:,.1f}"


def kelvin_fahrenheit (temperatura: float):

    temperatura_fahrenheit = (temperatura - 273.15) * 9 / 5 + 32

    return f"{temperatura_fahrenheit:,.1f}"


def kelvin_celsius (temperatura: float):

    temperatura_celsius = temperatura - 273.15

    return f"{temperatura_celsius:,.1f}"


def kelvin_rankine (temperatura: float):

    temperatura_rankine = temperatura * 9 / 5

    return f"{temperatura_rankine:,.1f}"


def rankine_fahrenheit (temperatura: float):

    temperatura_fahrenheit = temperatura - 459.67

    return f"{temperatura_fahrenheit:,.1f}"


def rankine_celsius (temperatura: float):

    temperatura_celsius = (temperatura - 491.67) * 5 / 9

    return f"{temperatura_celsius:,.1f}"


def rankine_kelvin (temperatura: float):

    temperatura_kelvin = temperatura * 5 / 9

    return f"{temperatura_kelvin:,.1f}"