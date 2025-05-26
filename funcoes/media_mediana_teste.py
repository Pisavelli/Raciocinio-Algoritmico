import media_mediana

numeros_par = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

media_par = media_mediana.calcular_media(numeros_par)
mediana_par = media_mediana.calcular_mediana(numeros_par)

print(f"A média e mediana da lista de números com quantidade par é:\nMédia: {media_par} | Mediana: {mediana_par}\n")

numeros_impar = [1, 2, 3, 4, 5, 6, 7, 8, 9]

media_impar = media_mediana.calcular_media(numeros_impar)
mediana_impar = media_mediana.calcular_mediana(numeros_impar)

print(f"A média e mediana da lista de números com quantidade ímpar é:\nMédia: {media_impar} | Mediana: {mediana_impar}")
