materiais_scp = []

print("--- Cadastro de 3 Materiais SCP ---")

for i in range(3):
    nome_mat = input(f"Digite o nome do material {i+1}: ")
    materiais_scp.append(nome_mat)
print("\n--- Materiais Cadastrados ---")
print(materiais_scp) # Mostra a lista inteira
