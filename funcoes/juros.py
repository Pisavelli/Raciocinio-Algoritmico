def juros_simples(capital, taxa, tempo):
    juros = capital * taxa * tempo
    montante = capital + juros
    return juros, montante

def juros_composto(capital, taxa, tempo):
    montante = capital * (1 + taxa) ** tempo
    juros = montante - capital
    return montante, juros
