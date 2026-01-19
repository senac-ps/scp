opcao = ""

while opcao != "S":
    print("\n-----Menu SPC ------")
    print("\n1- Cadrastra Bloco")
    print("2- Pedidos")
    print("s- Sair")
    opcao = input("Escolha uma opção: ").upper()
    if opcao == "1":
        print("--Abrindo Cadrastro de Bloco--")
    elif opcao == "2":
        print("--Abrindo Pedidos--")
    elif opcao == "S":
        print("--Saindo do sistema--")
    else:
        print("--Opção Invalida--")
print("\nFim do programa")


