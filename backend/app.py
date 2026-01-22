from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
from settings import TIPOS_PERMITIDOS, STATUS_PERMITIDOS
app = Flask(__name__)
CORS(app)

DB_NAME = "database.db"

# conexão com o banco
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


# cria tabela se não existir
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            tipo TEXT NOT NULL,
            status TEXT NOT NULL,
            descricao TEXT,
            data TEXT
        )
    """)
    conn.commit()
    conn.close()


# rota teste
@app.route("/")
def home():
    return jsonify({"message": "API Biblioteca funcionando 🚀"})


# GET /items — listar livros
@app.route("/items", methods=["GET"])
def get_items():
    conn = get_db_connection()
    items = conn.execute("SELECT * FROM items").fetchall()
    conn.close()

    lista = [dict(item) for item in items]
    return jsonify(lista), 200


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
