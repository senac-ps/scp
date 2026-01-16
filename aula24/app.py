from flask import Flask, jsonify

# Inicializar a aplicação Flask
app = Flask(__name__)

# Classe Material com POO
class Material:
    def __init__(self, id, nome, preco_m2):
        self.id = id
        self.nome = nome
        self.preco_m2 = preco_m2

    # O "Tradutor" para JSON (Dicionário)
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "preco_m2": self.preco_m2
        }

# Dados falsos com POO
m1 = Material(1, "Amarelo Ornamental", 150.0)
m2 = Material(2, "Verde Ubatuba", 220.5)
m3 = Material(3, "Branco Itaúnas", 450.0)

# A lista ÚNICA de Objetos
lista_de_materiais = [m1, m2, m3]

# Rota para listar TODOS os materiais
@app.route("/api/materiais")
def get_materiais():
    # 1. Criar uma lista de dicionários vazia
    materiais_em_dict = []

    # 2. Loop "inteligente"
    for mat in lista_de_materiais:
        # 3. Traduzir (chamar o método) e adicionar
        materiais_em_dict.append(mat.to_dict())

    # 4. Retornar a lista TRADUZIDA
    return jsonify(materiais_em_dict)

# Rota Dinâmica para buscar UM material específico por ID
@app.route("/api/materiais/<int:id>")
def get_material_por_id(id):
    # Loop para procurar o material com o ID correspondente
    for mat in lista_de_materiais:
        if mat.id == id:
            # Achamos! Retornar o material traduzido
            return jsonify(mat.to_dict())
    
    # Se não achar, retornar erro 404
    return jsonify({"erro": "Material não encontrado"}), 404

# A "Ignição" do servidor
if __name__ == "__main__":
    # Ligar o servidor em modo "Debug" (reinicia sozinho)
    app.run(debug=True)
