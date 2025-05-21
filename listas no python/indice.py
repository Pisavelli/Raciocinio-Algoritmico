a = []

for i in range(10):
    num = int(input(f"Digite o {i + 1}° inteiro: "))
    a.append(num)

print(a)

for i in range(len(a)):
    print(f"Índice: {i}; Valor: {a[i]}")
