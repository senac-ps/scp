def Cadastra():
    materiais_scp = []
    for i in range(3):
        nome_mat = input(f"Material {i+1}: ")
        materiais_scp.append(nome_mat)
    return materiais_scp 
    
def listar(listar_para_imprimir):
    print("\n--- Materiais  Cadastrados ---")
    for mat in listar_para_imprimir:
        print(f"{mat}")
print("Iniciando o Programa...")
listar_pricipal = Cadastra()
listar(listar_pricipal)