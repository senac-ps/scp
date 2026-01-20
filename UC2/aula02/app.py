from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# --- CONFIGURAÇÃO DA CONEXÃO ---
# Função para não repetir código toda hora
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",      
        database="senac_scp" #
    )

# --- ROTA 1: LISTAR TODOS OS MATERIAIS (GET) ---
@app.route("/api/materiais", methods=["GET"])
def get_materiais():
    # 1. Conectar
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 2. Executar (Ler a tabela inteira)
    cursor.execute("SELECT * FROM tbl_material")
    
    # 3. Pegar as Tuplas (ex: [(1, 'Granito', 100), (2, 'Marmore', 200)])
    resultados_tuplas = cursor.fetchall() #
    
    # 4. Fechar
    cursor.close()
    conn.close()
    
    # 5. Traduzir (Tupla -> Dicionário)
    lista_de_materiais = []
    for mat_tupla in resultados_tuplas:
        material_dict = {
            "id": mat_tupla[0],       # Coluna id_material
            "nome": mat_tupla[1],     # Coluna nome_mat
            "preco_m2": float(mat_tupla[2]) 
        }
        lista_de_materiais.append(material_dict)
        
    return jsonify(lista_de_materiais), 200

# --- ROTA 2: CADASTRAR PEDRA NOVA (POST) ---
@app.route("/api/materiais", methods=["POST"])
def create_material():
    # 1. Pegar o JSON do Insomnia
    nova_pedra = request.json
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 2. Query Segura (Evita SQL Injection com %s)
    # - Usando 'nome_mat'
    sql = "INSERT INTO tbl_material (nome_mat, preco_m2) VALUES (%s, %s)"
    
    # 3. Montar a Tupla de Valores
    valores = (nova_pedra["nome"], nova_pedra["preco_m2"])
    
    # 4. Executar
    cursor.execute(sql, valores) #
    
    # 5. COMMIT (Obrigatório para salvar no banco!)
    conn.commit() #
    
    # 6. Pegar o ID gerado automaticamente
    id_gerado = cursor.lastrowid #
    
    cursor.close()
    conn.close()
    
    # Devolver com o ID real
    nova_pedra["id"] = id_gerado
    return jsonify(nova_pedra), 201

# --- ROTA 3: BUSCAR MATERIAL POR ID (GET ID) ---
@app.route("/api/materiais/<int:id_busca>", methods=["GET"])
def get_one_material(id_busca):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Busca Específica (WHERE)
    sql = "SELECT * FROM tbl_material WHERE id_material = %s"
    
    # A vírgula é OBRIGATÓRIA na tupla de 1 item: (id, )
    cursor.execute(sql, (id_busca, )) 
    
    # Pegar SÓ UM resultado (não uma lista)
    mat_encontrado = cursor.fetchone() #
    
    cursor.close()
    conn.close()
    
    if mat_encontrado:
        material_dict = {
            "id": mat_encontrado[0],
            "nome": mat_encontrado[1], 
            "preco_m2": float(mat_encontrado[2])
        }
        return jsonify(material_dict), 200
    else:
        return jsonify({"erro": "Material não encontrado no estoque"}), 404

# --- ROTA 4: ATUALIZAR MATERIAL (PUT) ---
@app.route("/api/materiais/<int:id_busca>", methods=["PUT"])
def update_material(id_busca):
    # 1. Pegar os dados novos do JSON
    dados_novos = request.json
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 2. Query de Atualização (UPDATE ... WHERE)
    # Importante: Atualiza nome_mat e preco_m2 onde o id_material for igual ao da URL
    sql = "UPDATE tbl_material SET nome_mat = %s, preco_m2 = %s WHERE id_material = %s"
    
    # 3. Montar a Tupla (Nome Novo, Preço Novo, ID da URL)
    valores = (dados_novos["nome"], dados_novos["preco_m2"], id_busca)
    
    # 4. Executar
    cursor.execute(sql, valores)
    
    # 5. COMMIT (Obrigatório para salvar a alteração!)
    conn.commit()
    
    # 6. Verificar se alguma linha foi afetada
    linhas_afetadas = cursor.rowcount
    
    cursor.close()
    conn.close()
    
    if linhas_afetadas > 0:
        dados_novos["id"] = id_busca
        return jsonify(dados_novos), 200
    else:
        return jsonify({"erro": "Material não encontrado para atualizar"}), 404

# --- ROTA 5: DELETAR MATERIAL (DELETE) ---
@app.route("/api/materiais/<int:id_busca>", methods=["DELETE"])
def delete_material(id_busca):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 1. Query de Exclusão
    sql = "DELETE FROM tbl_material WHERE id_material = %s"
    
    # 2. Executar (Lembre da vírgula na tupla de 1 item)
    cursor.execute(sql, (id_busca, ))
    
    # 3. COMMIT (Obrigatório para confirmar a exclusão!)
    conn.commit()
    
    # 4. Verificar se apagou mesmo
    linhas_afetadas = cursor.rowcount
    
    cursor.close()
    conn.close()
    
    if linhas_afetadas > 0:
        return jsonify({"mensagem": "Material deletado com sucesso!"}), 200
    else:
        return jsonify({"erro": "Material não encontrado para deletar"}), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)