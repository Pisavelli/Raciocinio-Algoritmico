import operacoes

num = [float(input(f"Digite o {i + 1}º número: ")) for i in range(2)]

soma, sub = operacoes.operacoes_basicas(num[0], num[1])

mult, div = operacoes.operacoes_avancadas(num[0], num[1])

print(f"A soma dos números {num[0]} e {num[1]} é {soma}.\n")
print(f"A subtração dos números {num[0]} e {num[1]} é {sub}.\n")

print(f"A multiplicação de {num[0]} por {num[1]} é {mult}.\n")
print(f"A divisão de {num[0]} por {num[1]} é {div}.\n")
