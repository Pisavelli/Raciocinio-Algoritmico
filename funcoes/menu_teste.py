import menu, operacoes, verificador, horas

while True:
    menu.exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Você escolheu: Somar, subtrair, multiplicar e dividir dois números\n")

        num = [float(input(f"Digite o {i + 1}º número: ")) for i in range(2)]

        soma, sub = operacoes.operacoes_basicas(num[0], num[1])

        mult, div = operacoes.operacoes_avancadas(num[0], num[1])

        print(f"A soma dos números {num[0]} e {num[1]} é {soma}.\n")
        print(f"A subtração dos números {num[0]} e {num[1]} é {sub}.\n")

        print(f"A multiplicação de {num[0]} por {num[1]} é {mult}.\n")
        print(f"A divisão de {num[0]} por {num[1]} é {div}.\n")

    elif opcao == "2":
        print("Você escolheu: Verificar se número é par e primo\n")

        num = int(input("Digite um número inteiro: "))

        if verificador.if_par(num):
            print(f"{num} é par.\n")
        else:
            print(f"{num} é ímpar.\n")

        if verificador.if_primo(num):
            print(f"{num} é primo.\n")
        else:
            print(f"{num} não é primo.\n")

    elif opcao == "3":
        print("Você escolheu: Converter horas em minutos e segundos\n")

        horario = int(input("Digite as horas que deseje que sejam convertidas para minutos e segundos.\n"))

        minutos, segundos = horas.calcular_horas(horario)

        print(f"Este horário convertido fica assim:\nMinutos: {minutos} | Segundos: {segundos}\n")

    elif opcao == "4":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.\n")
