salarioAtual = float(input("Digite o salário atual: "))
tempoServico = int(input("Digite o tempo de serviço em anos: "))
if tempoServico > 5:
    print("Bônus concedido")
    salarioBonus = salarioAtual + (salarioAtual * 0.05)
    print(salarioBonus)
else:
    print("Bônus negado")