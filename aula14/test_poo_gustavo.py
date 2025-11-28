class Bloco:
    def __init__(self, codigo, preco_m2, largura, altura):
        self.codigo = codigo
        self.preco_m2 = preco_m2 
        self.largura = largura
        self.altura = altura

    def calcular_m2(self):
        m2 = self.largura * self.altura
        return m2

# --- FIM DA CLASSE ---

# 1. Criando o b1 com INPUTS (Interativo)
print("--- Novo Bloco ---")
cod_in = input("Digite o Código: ")
preco_in = float(input("Digite o Preço do m2: ")) # Converte texto para número decimal
larg_in = float(input("Digite a Largura: "))
alt_in = float(input("Digite a Altura: "))

b1 = Bloco(cod_in, preco_in, larg_in, alt_in)

# O b2 vou deixar fixo só pra gente ter mais de um na lista
b2 = Bloco("B-02", 220.5, 3.1, 2.0)

# 2. A Lista ÚNICA
lista_de_blocos = []

# 3. Adicionando os objetos
lista_de_blocos.append(b1)
lista_de_blocos.append(b2)

# 4. Percorrendo e calculando
print("\n--- Resultado Final ---")

for bloco in lista_de_blocos:
   print(f"Código: {bloco.codigo}")
   
   # O objeto sabe calcular a própria conta com os dados que você digitou
   m2_calculado = bloco.calcular_m2()
   print(f"  Metros Quadrados: {m2_calculado:.2f} m2")
