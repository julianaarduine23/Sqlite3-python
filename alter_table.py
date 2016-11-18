import sqlite3

conn = sqlite3.connect(r'C:\Users\ju\Desktop\esof\clientes.db')
cursor = conn.cursor()

#adicionando uma nova coluna na tabela clientes

cursor.execute("""
ALTER TABLE clientes
ADD COLUMN bloquado BOOLEAN;
""")

conn.commit()

print('Novo campo adicionado com sucesso.')

conn.close()
