def cadastrar():
    materiais_scp = []

    for i in range(3):
        nome_mat = input(f"Material  {i+1}: ")
        materiais_scp.append(nome_mat)

    return materiais_scp
 
def listar(lista_para_imprimir):
    print("\n--- Materiais Cadastrados ---")

    for mat in lista_para_imprimir:
        print(f"-> {mat}")

print("Iniciando o programa...")
lista_principal = cadastrar()
listar(lista_principal)
