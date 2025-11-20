# 1. A primeira leitura (fora do loop)
qualidade = int(input("Digite a Qualidade (1, 2 ou 3): "))
# 2. O "Segurança"
while qualidade < 1 or qualidade > 3:
 print("ERRO! Valor inválido. Tente novamente.")
 # 3. A "saída de emergência" (leitura de novo)
 qualidade = int(input("Digite 1, 2 ou 3: "))
# 4. Se saiu do loop, está correto.
print("Sucesso! Qualidade VÁLIDA registrada.")