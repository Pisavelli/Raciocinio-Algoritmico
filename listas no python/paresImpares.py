numeros = [int(input(f"Digite o {i+1}º número: ")) for i in range(5)]

pares = [num for num in numeros if num % 2 == 0]

impares = [num for num in numeros if num % 2 != 0]

print("\nResultados:")
print(f"Maior número par: {max(pares) if pares else 'Nenhum número par'}")
print(f"Menor número ímpar: {min(impares) if impares else 'Nenhum número ímpar'}")
print(f"Somatório dos elementos: {sum(numeros)}")
print(f"Média dos elementos: {sum(numeros) / len(numeros):.2f}")
