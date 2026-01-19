# --- Gaveteiros (Listas Paralelas) ---

codigos_blocos = []
precos_blocos = []

# --- Definições (Receitas) ---

def mostrar_menu():
    print("\n=== MENU SCP v3 ===")
    print("1. Cadastrar Bloco")
    print("2. Listar Blocos")
    print("S. Sair")

def cadastrar_bloco():
    print("\n--- Cadastrar Bloco ---")

    # Solicitar e validar código
    codigo = input("Código do bloco: ")
    if codigo == "":
        print("Código não pode ser vazio!")
        return
    
    # Solicitar e validar preço
    preco = float(input("Preço por m²: R$ "))
    
    if preco <= 0:
        print("Preço deve ser maior que zero!")
        return
    
    # Inserir na varável global
    codigos_blocos.append(codigo)
    precos_blocos.append(preco)
    
    # Mensagem sucesso
    print(f"Bloco {codigo} cadastrado com sucesso!")

def listar_blocos():
    print("\n--- Blocos Cadastrados ---")

    if len(codigos_blocos) == 0:
        print("Nenhum bloco cadastrado ainda.")
        return
    
    for i in range(len(codigos_blocos)):
        codigo = codigos_blocos[i]
        preco = precos_blocos[i]
        print(f"{i+1}. Código: {codigo} | Preço: R$ {preco:.2f}/m²")

# --- Loop Principal (Motor do Sistema) ---

def main():
    opcao = ""
    while opcao != "S":
        mostrar_menu()
        opcao = input("\nEscolha uma opção: ").upper()

        if opcao == "1":
            cadastrar_bloco()
        elif opcao == "2":
            listar_blocos()
        elif opcao == "S":
            print("\nObrigado por usar o SCP v3!")
        else:
            print("\nOpção inválida!")

# --- PONTO DE INÍCIO ---

main()