from flask import Flask, jsonify, request  # Importando 'request' para ler o Body

app = Flask(__name__)

# --- 1. O Modelo (A Classe) ---
class Material:
    def __init__(self, id, nome, preco_m2):
        self.id = id
        self.nome = nome
        self.preco_m2 = preco_m2

    def to_dict(self):
        """Converte o objeto para Dicionário (para virar JSON depois)"""
        return {"id": self.id, "nome": self.nome, "preco_m2": self.preco_m2}

# --- 2. O "Banco de Dados" (A Mentira/Memória) ---
lista_de_materiais = [
    Material(1, "Granito Cinza Andorinha", 250.00),
    Material(2, "Mármore Travertino", 450.00),
    Material(3, "Ardósia", 80.00)
]

# --- 3. As Rotas (O Garçom) ---

# Rota LEITURA GERAL (Read)
@app.route("/api/materiais", methods=["GET"])
def get_all_materiais():
    # Converte cada objeto da lista para dicionário
    lista_dict = [mat.to_dict() for mat in lista_de_materiais]
    return jsonify(lista_dict), 200

# Rota CRIAÇÃO (Create) - NOVIDADE DA AULA
@app.route("/api/materiais", methods=["POST"])
def create_material():
    # 1. Ler a "carta" (JSON) que chegou no Body
    dados = request.json 
    
    # 2. "Fabricar" o novo objeto
    # Gambiarra do ID: Pega o tamanho da lista + 1
    novo_id = len(lista_de_materiais) + 1
    
    novo_material = Material(
        id=novo_id,
        nome=dados["nome"],       # Pega do JSON enviado pelo Insomnia
        preco_m2=dados["preco_m2"]
    )
    
    # 3. Adicionar na lista (Salvar na memória)
    lista_de_materiais.append(novo_material)
    
    # 4. Responder com o que foi criado e Status 201 (Created)
    return jsonify(novo_material.to_dict()), 201

# Rota DINÂMICA (Read One, Update, Delete) - REFATORADA
@app.route("/api/materiais/<int:id>", methods=["GET", "PUT", "DELETE"]) #
def gerenciar_material_unico(id):
    
    # Passo 1: Achar o material na lista (comum a todos os verbos)
    mat_encontrado = None
    for mat in lista_de_materiais:
        if mat.id == id:
            mat_encontrado = mat
            break # Parar de procurar se achou

    # Se varreu a lista e não achou nada:
    if mat_encontrado is None:
        return jsonify({"erro": "Material não encontrado"}), 404

    # Passo 2: Decidir o que fazer com base no verbo HTTP
    
    # --- CENÁRIO A: É apenas leitura (GET) ---
    if request.method == "GET":
        return jsonify(mat_encontrado.to_dict()), 200

    # --- CENÁRIO B: É exclusão (DELETE) ---
    elif request.method == "DELETE": #
        lista_de_materiais.remove(mat_encontrado)
        return jsonify({"msg": f"Material {id} deletado com sucesso!"}), 200

    # --- CENÁRIO C: É atualização (PUT) ---
    elif request.method == "PUT": #
        dados = request.json # Ler os novos dados do Body
        
        # Atualizar os atributos do objeto encontrado
        mat_encontrado.nome = dados.get("nome", mat_encontrado.nome)
        mat_encontrado.preco_m2 = dados.get("preco_m2", mat_encontrado.preco_m2)
        
        return jsonify(mat_encontrado.to_dict()), 200

if __name__ == "__main__":
    app.run(debug=True)