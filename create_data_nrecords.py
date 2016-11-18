import sqlite3

conn = sqlite3.connect(r'C:\Users\ju\Desktop\esof\clientes.db')

cursor = conn.cursor()

#Criando uma lista de dados

lista = [(
'Fabio', 23, '44444444444', 'fabio@email.com', '1234-5678', 'Belo Horizonte', 'MG', '2014-06-09'),
('Joao', 21, '55555555555', 'joao@email.com',
'11-1234-5600', 'Sao Paulo', 'SP', '2014-06-09'),
('Xavier', 24, '66666666666', 'xavier@email.com', '12-1234-5601', 'Campinas', 'SP', '2014-06-10')]

#Inserindo dados na tabela

cursor.executemany("""
INSERT INTO clientes ( nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES (?,?,?,?,?,?,?,?)
""",lista)

conn.commit()
print('Dados inseridos com sucesso.')
conn.close()
