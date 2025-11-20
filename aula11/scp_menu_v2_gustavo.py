opcao = ""

while opcao != "S":
    print("\n--- SCP MENU (Python) ---")
    print(" 1 - Cadastros")
    print(" 2 - Pedidos")  
    print(" S - Sair")
    
    opcao = input("\nDigite sua opção: ").upper()
    
    if opcao == "1":
        print("\n...Abrindo menu de Cadastros...")
    elif opcao == "2":
        print("\n...Abrindo menu de Pedidos...")
    elif opcao == "S":
        print("\n...Saindo...")
    else:
        print("\nERRO: Opção inválida!")

print("Programa encerrado.")