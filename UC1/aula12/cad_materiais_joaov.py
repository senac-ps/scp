materiais = []

print("Materiais")

for i in range(3):
    nome_material = input(f"Digite o nome do material {i+1}:   ")
    materiais.append(nome_material)

print("\n Resultado")    
for mat in materiais:
    print(f"- {mat}")

