# Frequência de letras em uma frase

def contar_frequencia(frase):
    frase = frase.replace(" ", "").lower()
    frequencia = {}

    for letra in frase:
        if letra in frequencia:
            frequencia[letra] += 1
        else:
            frequencia[letra] = 1
    return frequencia

frase = input("Digite uma frase:\n")

resultado = contar_frequencia(frase)

print("\nFrequência de cada letra:")
print(resultado)
