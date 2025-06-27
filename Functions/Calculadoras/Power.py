def kw_cv (kilowatts: float):

    cv = kilowatts * 1.36

    return cv


def cv_kw (cavalos: float):

    kw = cavalos / 1.36

    return kw


def consumo_aparelho (volts: float, amperes: float):

    return volts * amperes