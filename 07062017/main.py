import math

unidades = {
    1: "um",
    2: "dois",
    3: "três",
    4: "quatro",
    5: "cinco",
    6: "seis",
    7: "sete",
    8: "oito",
    9: "nove"
}

dezenas = {
    10: "dez",
    11: "onze",
    12: "doze",
    13: "treze",
    14: "quatorze",
    15: "quinze",
    16: "dezesseis",
    17: "dezessete",
    18: "dezoito",
    19: "dezenove",
    20: "vinte",
    30: "trinta",
    40: "quarenta",
    50: "cinquenta",
    60: "sessenta",
    70: "setenta",
    80: "oitenta",
    90: "noventa"
}


def por_extenso2(inteiro, sufixo):
    extenso = ""
    if inteiro >= 10 and inteiro <= 19:
        extenso += "{} {}".format(
            dezenas.get(inteiro),
            sufixo)
    elif inteiro > 19:
        dezena_decimal = 10 * int(inteiro / 10)
        unidade_decimal = inteiro % 10
        if unidade_decimal:
            extenso += "{} e {} {}".format(
                dezenas.get(dezena_decimal),
                unidades.get(unidade_decimal),
                sufixo)
        else:
            extenso += "{} {}".format(
                dezenas.get(dezena_decimal),
                sufixo)
    else:
        extenso += "{} {}".format(unidades.get(inteiro), sufixo)

    return extenso


def por_extenso(numero):
    numero_decimal = math.ceil(100 * (numero - int(numero)))
    numero_inteiro = int(numero)

    extenso = ""

    if numero_inteiro:
        sufixo = "real" if numero_inteiro == 1 else "reais"

        extenso += por_extenso2(numero_inteiro, sufixo)

    print(extenso)
    if numero_decimal:
        if extenso:
            extenso += " e "
        sufixo = "centavo" if numero_decimal == 1 else "centavos"

        print(numero_decimal)
        extenso += por_extenso2(numero_decimal, sufixo)

    print(extenso)
    return extenso
