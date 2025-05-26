quantidade = int(input("Digite a quantidade de alunos na turma: "))
aprovado = 0
repetente = 0
for i in range(quantidade):
    media = float(input(f"Digite a média do {i + 1}° aluno (0 à 100): "))
    if media >= 60:
        aprovado += 1
    else:
        repetente += 1

print(f"A quantidade de alunos aprovados é {aprovado}. A quantidade de alunos repetentes é {repetente}.")
