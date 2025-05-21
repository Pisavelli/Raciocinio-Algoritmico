# Estoque de produtos

def estoque(quantidade):
    return "Em estoque." if quantidade > 0 else "Falta em estoque."

def atualizar_estoque(produto, quantidade_comprada):
    if produto in produtos:
        if produtos[produto] >= quantidade_comprada:
            produtos[produto] -= quantidade_comprada
            print(f"\nCompra realizada! {quantidade_comprada} unidades de {produto} foram retiradas do estoque.")
        else:
            print("\nEstoque insuficiente para essa compra!")
    else:
        print("\nProduto não encontrado.")

produtos = {}

quantidade = int(input("Quantos produtos deseja adicionar ao banco de dados?\n"))

while quantidade == 0:
    print("Quantidade inválida. Tente novamente.")
    quantidade = int(input("Quantos produtos deseja adicionar ao banco de dados?\n"))

for i in range(quantidade):
    nome = input(f"Digite o nome do produto {i+1}: ").upper()
    qtd = int(input(f"Digite a quantidade de {nome}: "))
    produtos[nome] = qtd

while True:
    print("\nEscolha uma ação:")
    print("1. Buscar produto")
    print("2. Realizar compra")
    print("3. Sair")
    
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        busca = input("\nDigite o nome do produto que deseja buscar:\n").upper()
        if busca in produtos:
            print(f"\nProduto: {busca}")
            print(f"Quantidade: {produtos[busca]}")
            print(f"Situação: {estoque(produtos[busca])}")
        else:
            print("Produto não encontrado.")
    
    elif opcao == "2":
        compra = input("\nDigite o nome do produto que deseja comprar:\n").upper()
        qtd_compra = int(input(f"Digite a quantidade de {compra} que deseja comprar:\n"))
        atualizar_estoque(compra, qtd_compra)
    
    elif opcao == "3":
        print("Finalizando programa...")
        break
    
    else:
        print("Opção inválida! Tente novamente.")
