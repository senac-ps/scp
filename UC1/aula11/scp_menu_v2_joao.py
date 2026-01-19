opcao=""
while opcao!= "S":
    print("\n--- SCP Menu (Python) ---")
    print(" 1 - Cadastro ")
    print(" 2 - Pedidos")
    print(" S - Sair")
    opcao = input ("Digite sua opção:").upper()
    if opcao =="1":
        print("...Abrindo menu Cadastros...")
    elif opcao == "2":
        print("...Abrindo menu de Pedidos...")
    elif opcao == "S":
        print("...Saindo...")
    else:
        print("Erro: Opção inválida!")
    print("Programa encerrado.")