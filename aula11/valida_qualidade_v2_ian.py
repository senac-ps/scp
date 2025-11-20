qualidade = int(input("Qualidade do produto:"))
while qualidade < 1 or qualidade > 3:
    qualidade = int(input("Tente De Novo: ")) 
    print("Sucesso")