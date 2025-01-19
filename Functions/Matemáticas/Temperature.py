def fahrenheit_celsius (temperatura: float):

    temperatura_celsius = (temperatura - 32) * 5 / 9

    return f"A temperatura em {temperatura:,.1f}° Fahrenheit equivale à {temperatura_celsius:,.1f}° Celsius"

def fahrenheit_kelvin (temperatura: float):

    temperatura_kelvin = (temperatura - 32) * 5 / 9 + 273.15

    return f"A temperatura em {temperatura:,.1f}° Fahrenheit equivale à {temperatura_kelvin:,.1f}° Kelvin"


def fahrenheit_rankine (temperatura: float):

    temperatura_rankine = temperatura + 459.67

    return f"A temperatura em {temperatura:,.1f}° Fahrenheit equivale à {temperatura_rankine:,.1f}° Rankine"


def celsius_fahrenheit (temperatura: float):

    temperatura_fahrenheit = (temperatura * 5 / 9) + 32

    return f"A temperatura em {temperatura:,.1f}° Celsius equivale à {temperatura_fahrenheit:,.1f}° Fahrenheit"


def celsius_kelvin (temperatura: float):

    temperatura_kelvin = temperatura + 273.15

    return f"A temperatura em {temperatura:,.1f}° Celsius equivale à {temperatura_kelvin:,.1f}° Kelvin"


def celsius_rankine (temperatura: float):

    temperatura_rankine = (temperatura - 491.67) * 5 / 9

    return f"A temperatura em {temperatura:,.1f}° Celsius equivale à {temperatura_rankine:,.1f}° Rankine"


def kelvin_fahrenheit (temperatura: float):

    temperatura_fahrenheit = (temperatura - 273.15) * 9 / 5 + 32

    return f"A temperatura em {temperatura:,.1f}° Kelvin equivale à {temperatura_fahrenheit:,.1f}° Fahrenheit"


def kelvin_celsius (temperatura: float):

    temperatura_celsius = temperatura - 273.15

    return f"A temperatura em {temperatura:,.1f}° Kelvin equivale à {temperatura_celsius:,.1f}° Celsius"


def kelvin_rankine (temperatura: float):

    temperatura_rankine = temperatura * 9 / 5

    return f"A temperatura em {temperatura:,.1f}° Kelvin equivale à {temperatura_rankine:,.1f}° Rankine"


def rankine_fahrenheit (temperatura: float):

    temperatura_fahrenheit = temperatura - 459.67

    return f"A temperatura em {temperatura:,.1f}° Rankine equivale à {temperatura_fahrenheit:,.1f}° Fahrenheit"


def rankine_celsius (temperatura: float):

    temperatura_celsius = (temperatura - 491.67) * 5 / 9

    return f"A temperatura em {temperatura:,.1f}° Rankine equivale à {temperatura_celsius:,.1f}° Celsius"


def rankine_kelvin (temperatura: float):

    temperatura_kelvin = temperatura * 5 / 9

    return f"A temperatura em {temperatura:,.1f}° Rankine equivale à {temperatura_kelvin:,.1f}° Kelvin"