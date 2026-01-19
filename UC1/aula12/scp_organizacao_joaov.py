def cadrastrar_materiais():
    materiais = []

    print("Cadastro de Materiais")  
    for i in range(3):
        nome_material = input(f"Digite o nome do material {i+1}:   ")
        materiais.append(nome_material)

    return materiais

def listar(materiais_para_imprimir):
    print("\nResultado")    
    for mat in materiais_para_imprimir:
        print(f"- {mat}")

print("Início do programa")

# Chama a função cadrastrar_materiais() para obter a lista de materiais
materiais_cadastrados = cadrastrar_materiais()

# Passa a lista de materiais para a função listar
listar(materiais_cadastrados)

print("Fim do programa")
