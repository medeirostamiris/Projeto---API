import sqlite3

DB_NAME = "database.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


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

def criar_item(titulo, tipo, status, descricao=None, data=None):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO items (titulo, tipo, status, descricao, data)
        VALUES (?, ?, ?, ?, ?)
    """, (titulo, tipo, status, descricao, data))

    conn.commit()
    conn.close()

def listar_items():
    conn = get_db_connection()
    items = conn.execute("SELECT * FROM items").fetchall()
    conn.close()
    return [dict(item) for item in items]
