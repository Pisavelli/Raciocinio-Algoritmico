# Cadastro e busca de notas de alunos

def calcular_media(notas):
    return sum(notas) / len(notas)

def determinar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

nota_alunos = {}

quantidade = int(input("Quantos alunos deseja registrar a nota?\n"))

while quantidade == 0:
    print("Quantidade inválida. Tente novamente.")
    quantidade = int(input("Quantos alunos deseja registrar a nota?\n"))

for i in range(quantidade):
    aluno = str(input("Digite o nome do aluno.\n")).upper()

    nota1 = float(input(f"Digite a 1º nota de {aluno}.\n"))
    while nota1 < 0 or nota1 > 10:
        print("Nota inválida. Digite uma nota entre 0 e 10.")
        nota1 = float(input(f"Digite novamente a 1º nota de {aluno}.\n"))

    nota2 = float(input(f"Digite a 2º nota de {aluno}.\n"))
    while nota2 < 0 or nota2 > 10:
        print("Nota inválida. Digite uma nota entre 0 e 10.")
        nota2 = float(input(f"Digite novamente a 2º nota de {aluno}.\n"))

    nota3 = float(input(f"Digite a 3º nota de {aluno}.\n"))
    while nota3 < 0 or nota3 > 10:
        print("Nota inválida. Digite uma nota entre 0 e 10.")
        nota3 = float(input(f"Digite novamente a 3º nota de {aluno}.\n"))

    nota_alunos[aluno] = [nota1, nota2, nota3]

print("\nAlunos com média maior ou igual a 7:")
for aluno, notas in nota_alunos.items():
    media = calcular_media(nota_alunos[aluno])
    if media >= 7:
        print(f"{aluno} -> Média: {media:.2f}")

while True:
    busca = input("\nDigite o nome do aluno que deseja buscar (ou 'SAIR' para finalizar).\n").upper()
    if busca == "SAIR":
        print("Finalizando busca...")
        break

    if busca in nota_alunos:
        media = calcular_media(nota_alunos[busca])
        situacao = determinar_situacao(media)

        print(f"\nAluno: {busca}")
        print(f"Média: {media:.2f}")
        print(f"Situação: {situacao}")
    else:
        print("Aluno não encontrado.")
