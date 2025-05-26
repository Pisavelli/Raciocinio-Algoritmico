def operacoes_basicas(num1, num2):
    soma = num1 + num2
    sub = num1 - num2
    return soma, sub

def operacoes_avancadas(num1, num2):
    mult = num1 * num2
    if num2 == 0:
        div = "Erro: divisão por zero."
    else:
        div = num1 / num2
    return mult, div
