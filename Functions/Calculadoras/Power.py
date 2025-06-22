def kw_cv (kilowatts: float):

    cv = kilowatts * 1.36

    return f"{cv:,.2f}"


def cv_kw (cavalos: float):

    kw = cavalos / 1.36

    return f"{kw:,.2f}"


def consumo_aparelho (volts: float, amperes: float):

    return f"{volts * amperes:,.2f}"