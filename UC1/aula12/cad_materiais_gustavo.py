# 1. Criar o "gaveteiro" (vazio)
materiais_scp = []
print("--- Cadastro de 3 Materiais SCP ---")

# 2. Usar o loop "contador" (Aula 11)
for i in range(3):
    nome_mat = input(f"Digite o nome do Material {i+1}: ")

    # 3. Adicionar na lista!
    materiais_scp.append(nome_mat)

# 4. Mostrar o resultado
print("\n--- Materiais Cadastrados ---")
for mat in materiais_scp:
    print(f"{mat}") # Mostra a lista inteira