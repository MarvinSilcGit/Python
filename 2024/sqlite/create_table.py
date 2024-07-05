import sqlite3

conn = sqlite3.conect('carros.db)
cursor = conn.cursos()

cursor.execute('''CREATE TABLE IF NOT EXISTS carros
(
    id INTEGER PRIMARY KEY,
    modelo TEXT NOT NULL,
    marca TEXT NOT NULL,
    ano INTEGER NOT NULL
))

conn.commit()
conn.close()
