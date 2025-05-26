def seguranca(senha):
    if len(senha) < 8:
        return False
    
    tem_letra = any(c.isalpha() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)

    return tem_letra, tem_numero
