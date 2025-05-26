import juros

#Juros Simples
js, ms = juros.juros_simples(1000, 0.05, 12)
print(f"Juros simples de capital de R$1.000,00, com 5% de taxa ao mês por um período de 12 meses.\nJuros Simples: R${js:.2f} | Montante: R${ms:.2f}\n")

#Juros Composto
jc, mc = juros.juros_composto(2500, 0.02, 24)
print(f"Juros compsto de capital de R$2.500,00, com 2% de taxa ao mês por um período de 24 meses.\nJuros Simples: R${jc:.2f} | Montante: R${mc:.2f}")