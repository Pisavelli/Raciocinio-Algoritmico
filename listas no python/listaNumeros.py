numeros = []
print("Insira os números um por um e digite 'fim' para finalizar:")
while True:
    entrada = input("Digite um número ou 'fim': ")
    if entrada.lower() == "fim":
        break
    try:
        numeros.append(float(entrada)) # Tentar converter a entrada para número e adicionar à lista
    except ValueError:
        print("Por favor, insira um número válido!")
if numeros:
    soma = 0
    for numero in numeros:
        soma += numero
    media = soma / len(numeros)
    print(f"A média dos números é: {media}")
else:
    print("Nenhum número foi inserido.")