import os

# Set up folder for notes
folder = "manipular arquivos"
os.makedirs(folder, exist_ok=True)

# Ask for note file name
note_name = input("Digite o nome do bloco de notas (sem espaços): ")
filename = f"{note_name}.txt"
filepath = os.path.join(folder, filename)

# Show existing content if file exists
def conteudo():
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return f.read()  # Return the content as a string
    else:
        return "\nO bloco de notas está vazio."  # Return a message if the file doesn't exist
    
print(f"\n--- Conteúdo no bloco de notas ---\n{conteudo()}")

# Ask user what to do
choice = input("\nVocê quer ADICIONAR conteúdo ao bloco de notas, REESCREVER o bloco de notas ou FINALIZAR?\n").upper()

while choice not in ["ADICIONAR", "REESCREVER", "FINALIZAR"]:
    choice = input("Escolha inválida. Você quer ADICIONAR conteúdo ao bloco de notas, REESCREVER o bloco de notas ou FINALIZAR?\n").upper()

if choice == "FINALIZAR":
    print("\nOperação finalizada pelo usuário. Nenhuma alteração foi feita.")
else:
    mode = "w" if choice == "REESCREVER" else "a"

    # Get new content
    new_text = input("\nDigite sua anotação:\n")

    # Write to file
    with open(filepath, mode) as f:
        f.write(new_text + "\n")

    print(conteudo())
    print(f"\nAnotação salva em {filepath}")
