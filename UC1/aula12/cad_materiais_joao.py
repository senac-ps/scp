materiais_scp = []
print("--- Cadastro de 3 Materiais SCP ---")
for i in range(3):
    nome_mat = input(f"Digite o nome Material {i+1}: ")
    materiais_scp.append(nome_mat)
print("\n--- Materiais Cadastrados ---")
for mat in materiais_scp:
    print(f"{mat}") 
