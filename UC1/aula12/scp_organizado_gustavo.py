def cadastrar():
    materiais_scp = []
    
    for i in range(3):
        nome_mat = input(f"Material {i+1}: ")
        materiais_scp.append(nome_mat)
    
    return materiais_scp  # "Devolve" a lista pronta

def listar(lista_para_imprimir):
    print("\n--- Materiais Cadastrados ---")
    
    for mat in lista_para_imprimir:
        print(f"-> {mat}")

# --- SCRIPT PRINCIPAL ---
# (Este é o único código que roda "solto")

print("Iniciando o programa...")

# 1. Chama o cadastro e pega o "retorno"
lista_principal = cadastrar()

# 2. Envia a lista principal como "parâmetro"  
listar(lista_principal)