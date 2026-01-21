# app.py
from flask import Flask
from flask_cors import CORS # Instale com: pip install flask-cors

# Importando os "Garçons Especialistas" (Blueprints)
from routes_materiais import bp_materiais
from routes_blocos import bp_blocos
from routes_clientes import bp_clientes

app = Flask(__name__)

# Aplicando o "Crachá" de segurança para o navegador aceitar chamadas
CORS(app) 

# Registrando as rotas no sistema principal
app.register_blueprint(bp_materiais)
app.register_blueprint(bp_blocos)
app.register_blueprint(bp_clientes)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)