from flask import Flask, jsonify # 1. Importar

# ... (app = Flask... e a rota principal...)
app = Flask(__name__)
@app.route("/")
def rota_principal():
    # A "Bandeja" de resposta
    return "Bem-vindo a API do SCP!"

# 2. A Nova Rota (do "Cardápio")
@app.route("/api/materiais")
def get_materiais():
    # 3. Dados "Falsos" (Mockados) - (Ainda não fomos na "Cozinha")
    dados_falsos = [
        {"id": 1, "nome": "Amarelo Ornamental", "preco_m2": 150.0},
        {"id": 2, "nome": "Verde Ubatuba", "preco_m2": 220.5},
        {"id": 3, "nome": "Branco Itaúnas", "preco_m2": 450.0}
    ]

    # 4. Retornar a "Bandeja" JSON
    return jsonify(dados_falsos)

# A "Ignição"
if __name__ == "__main__":
    # Ligar o servidor em modo "Debug" (reinicia sozinho)
    app.run(debug=True)