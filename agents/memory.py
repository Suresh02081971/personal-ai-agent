import sqlite3
import os

DB_PATH = "storage/memory.db"

def init_db():
    os.makedirs("storage", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_memory(text: str):
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO memory (content) VALUES (?)", (text,))
    conn.commit()
    conn.close()

def load_memory(limit: int = 5):
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "SELECT content FROM memory ORDER BY id DESC LIMIT ?",
        (limit,)
    )
    rows = cur.fetchall()
    conn.close()
    return [r[0] for r in rows]
