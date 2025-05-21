# Agenda de contatos

contatos = {}  # Dicionário para armazenar os contatos

while True:
    print("\nOpções:")
    print("1. Cadastrar contato")
    print("2. Buscar contato")
    print("3. Excluir contato")
    print("4. Listar todos os contatos")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do contato: ").upper()
        telefone = input("Digite o telefone do contato: ")
        contatos[nome] = telefone
        print("Contato cadastrado com sucesso!")

    elif opcao == "2":
        nome = input("Digite o nome do contato que deseja buscar: ").upper()
        if nome in contatos:
            print(f"\nContato encontrado: {nome} - {contatos[nome]}")
        else:
            print("Contato não encontrado.")

    elif opcao == "3":
        nome = input("Digite o nome do contato que deseja excluir: ").upper()
        if nome in contatos:
            del contatos[nome]
            print("Contato excluído com sucesso!")
        else:
            print("Contato não encontrado.")

    elif opcao == "4":
        print("\nLista de contatos:")
        if contatos:
            for nome, telefone in contatos.items():
                print(f"{nome}: {telefone}")
        else:
            print("Nenhum contato cadastrado.")

    elif opcao == "5":
        print("Finalizando programa...")
        break

    else:
        print("Opção inválida! Tente novamente.")
