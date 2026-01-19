class Bloco:
    def __init__(self, codigo, preco_m2, largura, altura):
        self.codigo = codigo
        self.preco_m2 = preco_m2
        self.largura = largura
        self.altura = altura
    def calcular_m2(self):
        m2 = self.largura * self.altura
        return m2
        