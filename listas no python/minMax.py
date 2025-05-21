a = []

for i in range(10):
    num = int(input(f"Digite o {i + 1}° inteiro: "))
    a.append(num)

minima = min(a)
maxima = max(a)
print(f"O menor valor da lista é {minima}. O maior valor da lista é {maxima}.")