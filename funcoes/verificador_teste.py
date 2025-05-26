import verificador

numero = int(input("Digite um número inteiro: "))

if verificador.if_par(numero):
    print(f"{numero} é par.")
else:
    print(f"{numero} é ímpar.")

if verificador.if_primo(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")
