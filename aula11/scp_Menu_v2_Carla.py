opcao = ""

while opcao != "S":
    print("\n--- SCP MENU (Python) ---")
    print(" 1 - Cadastros")
    print(" 2 - Pedidos")
    print(" S - Sair")

    opcao = input("Digite sua opção: ").upper()

    if opcao == "1":
        print("...Abrindo menu de Cadastros...")
    elif opcao == "2":
        print("...Abrindo menu de Pedidos...")
    elif opcao == "S":
        print("...Saindo...")
    else:
        print("ERRO: Opção inválida!")

print("Progama encerrado.")
