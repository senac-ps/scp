codigos_blocos = []
precos_blocos = []

def mostrar_menu():
    print("\n--- MENU PRINCIPAL ---")
    print("1 - Cadastrar Bloco")
    print("2 - Listar Blocos")
    print("S - Sair")

def cadastrar_bloco():
    print("\n--- CADASTRAR BLOCOS ---")
    print("\nCadastrar Código do Bloco")
    codigos = input("Digite o Código do Bloco:  ")

    if codigos == "":
        print("Código não pode ser vazio!")
        return

    precos = float(input("Digite o preço do Bloco:  "))

    if precos <= 0:
        print("Preços não pode ser menor ou zero!")
        return

    codigos_blocos.append(codigos)
    precos_blocos.append(precos)
    print("\n Códigos e Preços cadastrados!")

    print(f"Códigos: {codigos} Preços:{precos}")

def listar_blocos():
    print("\n--- LISTA DE BLOCOS NO PÁTIO ---")

    for i in range(len(codigos_blocos)):
        print(f" Codigo: {codigos_blocos[i]}")
        print(f" Preço R$ {precos_blocos[i]}")
        print("-----------------")

def main():
    opcao = ""
    while opcao != "S":
        mostrar_menu()
        opcao = input("Escolha uma opção do Menu:").upper()
        if opcao == "1":
            cadastrar_bloco()
        elif opcao == "2":
            listar_blocos()
        elif opcao == "S":
            print("Sair")
        else:
            print("Opção inválida")

main()