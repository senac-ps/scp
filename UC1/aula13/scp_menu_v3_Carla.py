codigos_blocos = []
precos_blocos = []

def mostrar_menu():
    pass 

def cadastrar_bloco():
    pass  

def listar_blocos():
    print("\n--- LISTA DE BLOCOS NO PÁTIO ---")
    
    fori in range(len(codigos_blocos)):
        print(f" Codigo: {codigos_blocos[i]}")
        print(f" Preço: R$ {precos_blocos[i]}")
        print("--------------------")

def main():
    opcao = ""
    while opcao != "S"
        opcao = mostrar_menu()
        if opcao == "1":
            cadastrar_bloco()
        elif opcao == "2":
            listar_blocos()
        elif opcao == "S":
            print("Sair")
        else:
            print(" opcao inválida")
    
main()
