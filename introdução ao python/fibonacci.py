N = int(input("Digite o número de termos da sequência de Fibonacci: "))

a, b = 0, 1

count = 0
while count < N:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
