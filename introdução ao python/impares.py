acumulador = 0
contador = 0
while contador <= 2:
    n = float(input("Digite um número. Se for negativo, o programa irá parar.\n"))
    if n < 0:
        break

    if n % 3 == 0:
        acumulador += n
        contador += 1

if contador > 0:
    media = acumulador / contador
    print(f"A soma dos números ímpares é: {acumulador}")
    print(f"A média dos números ímpares é: {media}")
else:
    print("Nenhum número par foi digitado.")
