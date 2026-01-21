# routes_materiais.py
from flask import Blueprint, jsonify, request
import mysql.connector

# Criando o Blueprint (O "Departamento" de Materiais)
bp_materiais = Blueprint("materiais", __name__, url_prefix="/api")

def get_db_connection():
    return mysql.connector.connect(
        host="localhost", user="root", password="", database="senac_scp"
    )

# --- ROTAS DE MATERIAIS (MIGRADAS DO SEU CÓDIGO) ---

@bp_materiais.route("/materiais", methods=["GET"])
def get_materiais():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tbl_material")
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    
    lista = []
    for mat in resultados:
        lista.append({
            "id": mat[0],
            "nome": mat[1], # nome_mat
            "preco_m2": float(mat[2])
        })
    return jsonify(lista), 200

@bp_materiais.route("/materiais", methods=["POST"])
def create_material():
    dados = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO tbl_material (nome_mat, preco_m2) VALUES (%s, %s)"
    cursor.execute(sql, (dados["nome"], dados["preco_m2"]))
    conn.commit()
    novo_id = cursor.lastrowid
    cursor.close()
    conn.close()
    dados["id"] = novo_id
    return jsonify(dados), 201

@bp_materiais.route("/materiais/<int:id>", methods=["PUT"])
def update_material(id):
    dados = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "UPDATE tbl_material SET nome_mat = %s, preco_m2 = %s WHERE id_material = %s"
    cursor.execute(sql, (dados["nome"], dados["preco_m2"], id))
    conn.commit()
    rows = cursor.rowcount
    cursor.close()
    conn.close()
    if rows > 0:
        dados["id"] = id
        return jsonify(dados), 200
    return jsonify({"erro": "Material não encontrado"}), 404

@bp_materiais.route("/materiais/<int:id>", methods=["DELETE"])
def delete_material(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tbl_material WHERE id_material = %s", (id,))
    conn.commit()
    rows = cursor.rowcount
    cursor.close()
    conn.close()
    if rows > 0:
        return jsonify({"msg": "Deletado com sucesso"}), 200
    return jsonify({"erro": "Não encontrado"}), 404