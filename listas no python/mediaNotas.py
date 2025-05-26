alunos = []

for i in range(50):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    alunos.append((nome, nota))

soma_das_notas = sum(nota for i, nota in alunos)
media = soma_das_notas / len(alunos)

print(f"A média das notas dos 50 alunos é: {media:.2f}")
