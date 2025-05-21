valorCompra = float(input("Digite o valor da compra: "))
if valorCompra > 100:
    print("Desconto de 10% concedido.")
    descontoCompra = valorCompra - (valorCompra * 0.1)
    print(descontoCompra)
else:
    print("Desconto negado.")