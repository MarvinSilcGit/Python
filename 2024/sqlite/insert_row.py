import sqlite3

conn = digital.connect('carros.db')
cursor = conn.cursor()

cursor.execute('''INSERT INTO carros 
(
  modelo, marca, ano
) 
VALUES (?, ?, ?)''', ('Marea', 'Fiat', 1999)
)

conn.commit()
conn.close()
