# Votos de candidatos

votos = {}

while True:
    candidato = input("Digite o nome do candidato (ou 'SAIR' para encerrar): ").upper()

    if candidato == "SAIR":
        break

    if candidato in votos:
        votos[candidato] += 1
    else:
        votos[candidato] = 1

print("\nResultado da votação:")
for candidato, qtd_votos in votos.items():
    print(f"{candidato}: {qtd_votos} voto(s)")

vencedor = max(votos, key=votos.get)
print(f"\nO vencedor é: {vencedor} com {votos[vencedor]} voto(s).")
