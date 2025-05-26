numero = int(input("Insira um número inteiro positivo: "))
fatorial = 1
if numero < 0:
    print("Por favor, insira um número positivo.")
else:
    for i in range(1, numero + 1):
        fatorial *= i

print(f"O fatorial de {numero} é {fatorial}.")
