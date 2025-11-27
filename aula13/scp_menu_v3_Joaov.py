codigos_de_blocos = []
preco_blocos = []

def Mostra_menu():
        print("\n====== MENU ======")
        print("1 - Cadastrar Bloco")
        print("2 - Listar Blocos")
        print("S - Sair")
        
def cadastra_bloco():
    print("\n=== Cadastro de Blocos ===")

    # Entrada do código do bloco
    cod_bloco = input("Digite o código do bloco: ").strip()

    # Validação: o código não pode estar vazio
    while cod_bloco == "":
        print("❌ O código do bloco não pode ficar vazio!")
        cod_bloco = input("Digite o código do bloco: ").strip()

    # Entrada e validação do preço
    while True:
        try:
            preco_bloco = float(input("Digite o preço do bloco: "))

            # O preço deve ser maior que 1 (ou qualquer regra que você queira)
            if preco_bloco > 1:
                break
            else:
                print("❌ O preço deve ser maior que 1! Tente novamente.")
        except ValueError:
            print("❌ Valor inválido! Digite um número válido.")

    # Se chegou aqui, o bloco está validado e será cadastrado
    codigos_de_blocos.append(cod_bloco)
    preco_blocos.append(preco_bloco)

    print("\n✔️ --- Bloco Cadastrado com sucesso! ---")
    print(f"Código: {cod_bloco} Preço: R$ {preco_bloco}")
    

def  listar_blocos():
    print("\n--- Blocos Cadastrados ---")
    for i in range(len(codigos_de_blocos)):
        print(f"Codigo: {codigos_de_blocos[i]} Preço R$ {preco_blocos[i]}")
    
def main():
    opcao = ""

    while opcao != "S":
        Mostra_menu()
        
        opcao = input("Opção: ").upper().strip()

        if opcao == "1":
            cadastra_bloco()
        elif opcao == "2":
            listar_blocos()
        elif opcao == "S":
            print("Saindo...")
        else:
            print("❌ Opção inválida! Tente novamente.")

main()

       
       