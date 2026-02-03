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


# CREATE
def criar_item(titulo, tipo, status, descricao=None, data=None):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO items (titulo, tipo, status, descricao, data)
        VALUES (?, ?, ?, ?, ?)
    """, (titulo, tipo, status, descricao, data))

    conn.commit()
    item_id = cursor.lastrowid
    conn.close()

    return item_id


# READ (todos)
def listar_items():
    conn = get_db_connection()
    items = conn.execute("SELECT * FROM items").fetchall()
    conn.close()

    return [dict(item) for item in items]


# READ (por id)
def buscar_item(id):
    conn = get_db_connection()

    item = conn.execute(
        "SELECT * FROM items WHERE id = ?",
        (id,)
    ).fetchone()

    conn.close()

    if item:
        return dict(item)
    return None


# UPDATE (PUT)
def atualizar_item(id, titulo, tipo, status, descricao, data):
    conn = get_db_connection()

    conn.execute("""
        UPDATE items
        SET titulo = ?,
            tipo = ?,
            status = ?,
            descricao = ?,
            data = ?
        WHERE id = ?
    """, (titulo, tipo, status, descricao, data, id))

    conn.commit()
    conn.close()


# UPDATE (PATCH status)
def atualizar_status(id, status):
    conn = get_db_connection()

    conn.execute("""
        UPDATE items
        SET status = ?
        WHERE id = ?
    """, (status, id))

    conn.commit()
    conn.close()


# DELETE
def deletar_item(id):
    conn = get_db_connection()

    conn.execute(
        "DELETE FROM items WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()
