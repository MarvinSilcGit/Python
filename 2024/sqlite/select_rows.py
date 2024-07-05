import sqlite3

conn = sqlite3.connect('carros.db')

cursor = conn.cursor()

cursor.execute('SELECT * FROM carros')

registros = cursor.fetchall()

conn.close()

print(registros)
