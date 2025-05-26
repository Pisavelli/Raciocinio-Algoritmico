def calcular_media(lista):
    return sum(lista) / len(lista)

def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    meio = n // 2

    if n % 2 == 1: #Lista com número ímpar
        return lista_ordenada[meio]
    else: #Lista com número par
        return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2
