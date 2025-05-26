import strings_util

frase = "Hello, world!"

num_vogais = strings_util.contar_vogais(frase)
print(f"Número de vogais na frase '{frase}': {num_vogais}.")

invertida = strings_util.inverter_string(frase)
print(f"A frase '{frase}' invertida fica assim: '{invertida}'.")
