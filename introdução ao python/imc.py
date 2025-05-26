altura = float(input("Digite o altura em Metros (EXEMPLO - 1.75m): "))
peso = int(input("Digite o peso em Kilogramas: "))
imc = peso / (altura * altura)
print(imc)
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso ideal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")
