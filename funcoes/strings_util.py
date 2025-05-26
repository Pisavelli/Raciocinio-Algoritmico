def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    return sum(1 for letra in texto if letra in vogais)

def inverter_string(texto):
    return texto[::-1]
