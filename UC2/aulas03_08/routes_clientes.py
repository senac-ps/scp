# routes_clientes.py
from flask import Blueprint, jsonify, request
import mysql.connector

bp_clientes = Blueprint("clientes", __name__, url_prefix="/api")

def get_db_connection():
    return mysql.connector.connect(host="localhost", user="root", password="", database="senac_scp")

@bp_clientes.route("/clientes", methods=["GET"])
def get_clientes():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tbl_cliente")
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    
    lista = []
    for row in resultados:
        lista.append({
            "id": row[0],
            "nome": row[1],
            "cpf_cnpj": row[2],
            "telefone": row[3],
            "email": row[4]
        })
    return jsonify(lista), 200

@bp_clientes.route("/clientes", methods=["POST"])
def create_cliente():
    dados = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO tbl_cliente (nome_razao, cpf_cnpj, telefone, email) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (dados["nome"], dados["cpf_cnpj"], dados["telefone"], dados["email"]))
    conn.commit()
    dados["id"] = cursor.lastrowid
    cursor.close()
    conn.close()
    return jsonify(dados), 201