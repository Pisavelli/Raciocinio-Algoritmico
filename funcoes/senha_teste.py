import senha_seg

senha = input("Digite uma senha: ")

if senha_seg.seguranca(senha):
    print("Está senha é segura.")
else:
    print("Está senha possuí é fraca. Ela deve ter no mínimo 8 caracteres, letras e números.")
