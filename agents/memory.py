import sqlite3

DB_PATH = "storage/memory.db"

def save_memory(text: str):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS memory (content TEXT)")
    cur.execute("INSERT INTO memory VALUES (?)", (text,))
    conn.commit()
    conn.close()
