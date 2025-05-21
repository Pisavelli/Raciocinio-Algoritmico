salarioAnual = float(input("Digite seu salário anual: "))
if salarioAnual <= 20000:
    print("Sem alíquota.")
elif salarioAnual <= 50000:
    print("Alíquota de 15%.")
    salarioAnual = salarioAnual + (salarioAnual * 0.15)
    print(salarioAnual)
else:
    print("Alíquota de 25%.")
    salarioAnual = salarioAnual + (salarioAnual * 0.25)
    print(salarioAnual)