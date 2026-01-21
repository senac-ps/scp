# routes_blocos.py
from flask import Blueprint, jsonify, request
import mysql.connector

bp_blocos = Blueprint("blocos", __name__, url_prefix="/api")

def get_db_connection():
    return mysql.connector.connect(
        host="localhost", user="root", password="", database="senac_scp"
    )

# --- ROTA COM JOIN (AULA 06) ---
@bp_blocos.route("/blocos", methods=["GET"])
def get_blocos():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # O "Super-Select" para trazer o nome do material junto
    sql = """
    SELECT 
        tbl_bloco.id_bloco, 
        tbl_bloco.codigo, 
        tbl_bloco.largura,
        tbl_bloco.altura,
        tbl_bloco.profundidade,
        tbl_material.nome_mat,
        tbl_material.preco_m2
    FROM tbl_bloco
    LEFT JOIN tbl_material ON tbl_bloco.id_material_fk = tbl_material.id_material
    """
    cursor.execute(sql)
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    
    lista = []
    for row in resultados:
        lista.append({
            "id": row[0],
            "codigo": row[1],
            "dimensoes": f"{float(row[2])}x{float(row[3])}x{float(row[4])}",
            "material_nome": row[5], # AQUI ESTÁ O JOIN FUNCIONANDO!
            "material_preco": float(row[6])
        })
    return jsonify(lista), 200

@bp_blocos.route("/blocos", methods=["POST"])
def create_bloco():
    dados = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Inserindo com a FK (id_material_fk)
    sql = """INSERT INTO tbl_bloco (codigo, largura, altura, profundidade, id_material_fk) 
             VALUES (%s, %s, %s, %s, %s)"""
    
    valores = (dados["codigo"], dados["largura"], dados["altura"], dados["profundidade"], dados["id_material"])
    
    cursor.execute(sql, valores)
    conn.commit()
    dados["id"] = cursor.lastrowid
    cursor.close()
    conn.close()
    return jsonify(dados), 201