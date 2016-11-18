import os
import sqlite3
import io
import datetime
import names
import csv
from gen_random_values import *

class Connect(object):
    def _init_(self, db_name):
        try:
            #conectando...
            self.conn = sqlite.connect(db_name)
            self.cursor = self.conn.cursor()
            print("Banco:", db_name)
            self.cursor.execute('SELECT SQLITE_VERSION()')
        except sqlite3.Error:
            print("Erro ao abrir banco.")
            return False

    def commit_db(self):
        if self.conn:
            self.conn.commit()

    def close_db(self):
        if self.conn:
            self.conn.close()
            print("Conexão encerrada.")

class ClientesDb(object):
    tb_name = 'clientes'
    def _init_(self):
        self.db = Connect('clientes.db')
        self.tb_name

    def fechar_conexao(self):
        self.db.close_db()

if '_name_' == '_main_':
    c = ClientesDb()

def criar_schema(self, shema_name = 'sql/clientes.sql'):
    print("Criando tabela %s ..."% self.tb_name)
    try:
        with open(schema_name, 'rt') as f:
            schema = f.read()
            self.db.cursor.executescript(schema)
    except sqlite3.Error:
        print("Aviso: A tabela %s ja existe." % self.tb_name)
        return False

    print("Tabela %s criada com sucesso." % self.tb_name)

    ...
    if '_name_' == '_main_':
        c = ClientesDb()
        c.criar_schema()

def inserir_um_registro(self):
    try:
        self.db.cursor.execute("""
        INSERT INTO clientes (nome, idade, cpf, email,
        VALUES ('Regis da Silva', 35 '12345678901', 'regis@email.com', '(11) 9876-5342', 'São Paulo', 'SP','2014-07-30 11:23:00.199000')
        """)
        #Gravando no banco de dados
        self.db.commit_db()
        print("Um registro inserido com sucesso.")
    except sqlite3.IntegrityError:
        print("Aviso: O email deve ser único.")
        return False

    ...
if '_name_' == '_main_':
    c = ClientesDb()
    c.criar_schema()
    c.inserir_um_registro()


def inserir_com_lista(self):
    lista = [('Agenor de Souza', 23, '12345678901', 'agenor@email.com', '(10) 8300-0000', 'Salvador', 'BA', '2014-07-29 11:23:01.199001'),
    ('Bianca Antunes', 21, '12345678902','bianca@email.com', '(10) 8350-0001', 'Fortaleza', 'CE', '2014-07-28 11:23:02.199003'),
    ('Carla Ribeiro', 30, '12345678903', 'carla@email.com','(10) 8377-0002', 'Campinas', 'SP', '2014-07-28 11:23:03.199003'),
    ('Fabiana de Almeida', 25, '12345678904', 'fabiana@email.com', '(10) 8388-0003', 'São Paulo', 'SP', '2014-07-29 11:23:04.199004'),]
    try:
        self.db.cursor.executemany("""
        INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
        VALUES (?,?,?,?,?,?,?,?)
        """, lista)
        #gravando no bd
        self.db.commit_db()
        print("Dados inseridos da lista com sucesso: %s registros." % len(lista))
    except sqlite3.IntegrityError:
        print("Aviso: o email deve ser único")
        return False

def inserir_de_arquivo(self):
    try:
        with open('sql/clie ntes_dados.sql', 'rt') as f:
            dados = f.read()
            self.db.commit_db()
            print("Dados inseridos do arquivo com sucesso.")
    except sqlite3.IntegrityError:
        print("Aviso: o email deve ser unico.")
        return False

import csv
...
def inserir_de_csv(self, file_name = 'csv/clientes.csv'):
    try:
        reader = csv.reader(
            open(file_name,'rt'), delimiter =',')
        linha = (reader,)
        for linha in reader:
            self.db.cursor.execute("""
            INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
            VALUES (?,?,?,?,?,?,?,?)
            """, linha)
            # gravando no banco de dados
            self.db.commit_db()
            print("Dados importados do csv com sucesso.")
    except sqlite3.IntegrityError:
        print("Aviso: o email deve ser único.")
        return False

def inserir_com_parametros(self):
    #solicitando os dados ao usuario
    self.nome = input('Nome: ')
    self.idade = input('Idade: ')
    self.cpf = input('CPF: ')
    self.email = input('Email: ')
    self.fone = input('Fone: ')
    self.cidade = input('Cidade')
    self.uf = input('UF: ')
    date = datetime.datetime.now().isoformat(" ")
    self.criado_em = input('Criado em (%s): ' % date) or date
    try:
        self.db.cursor.execute("""
        INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
        VALUES (?,?,?,?,?,?,?,?)
        """, (self.nome, self.idade, self.cpf, self.email, self.fone, self.cidade, self.uf, self.criado_em))
        #gravando no banco no dados
        self.db.commit_db()
        print("Dados inseridos com sucesso.")
    except sqlite3.IntegrityError:
        print("Aviso: O email deve ser único.")
        return False

def inserir_randomico(self, repeat = 10):
    # Inserir registros com vaçpres randomicos names
    lista = []
    for _i in range(repeat):
        date = datetime.datetime.now().isoformat(" ")
        fname = names.get_first_name()
        lname = names.get_last_name()
        name = fname + ' ' + lname
        email = fname[0].lower() + '.' + lname.lower() + '@email.com'
        c = gen_city()
        city = c[0]
        uf = c[1]
        lista.append((name, gen_age(), gen_cpf(), email, gen_phone(), city, uf, date))
        try:
            self.db.cursor.execute("""
            INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, fone, cidade uf, criado_em)
            VALUES (?,?,?,?,?,?,?,?)
            """, lista)
            self.db.commit()
            print ("Inserindo %s registros na tebla..." % repeat)
            print("registros criado com sucesso.")
        except sqlite3.IntegrityError:
            print("Aviso: email deve ser único.")
            return False

def ler_todos_clientes(self):
    sql = 'SELECT * FROM clientes ORDER BY nome'
    r = self.db.cursor.execute(sql)
    return r.fetchall()

def imprimir_todos_clientes(self):
    lista = self.ler_todos_clientes()
    for c in lista:
        print(c)
def localizar_cliente(self,id):
    r = self.db.cursor.execute(
    'SELECR * FROM clientes WHERE id = ?', (id))
    return r.fetchone()             #fetchone retorna apenas uma linha de registros

def imprimir_cliente(self, id):
    if self.localizar_cliente(id) == None:
        print('Não existe cliente com o id informado.')
    else:
        print(self.localizar_cliente(id))

def contar_cliente(self):       #contando os registros
    r = self.db.cursor.execute(
    'SELECT COUNT(*) FROM clientes')
    print("Total de clientes:", r.fetchone()[0])

def contar_cliente_por_idade(self, t=50):       #Localizar clientes por idade
    r = self.db.cursor.execute(
    'SELECT COUNT (*) FROM clientes WHERE idade > ?', (t,))
    print ("Clientes maiores que", t, "anos:", r.fetchone() [0])

def localizar_cliente_por_uf(self, t = 'SP'):       #Localizando por UF
    resultado =self.db.cursor.execute('SELECT * FROM clientes WHERE uf = ?', (t,))
    print ("Clientes do estado de", t, ":")
    for cliente in resultado.fetchall():
        print(cliente)

def meu_select(self, sql="SELECT * FROM clientes WHERE uf='RJ';"):
    r = self.db.cursor.execute(sql)
    #gravando no bd
    self.db.commit_db()
    for cliente in r.fetchall():
        print(cliente)
        c.meu_select("SELECT * FROM clientes WHERE uf='MG' order by NOME;")

def ler_arquivo(self, file_name='sql/clientes_sp.sql'):
    with open (file_name, 'rt') as f:
        dados = f.read()
        sqlcomandos = dados.split(';')
        print("Consulta feita a partir de arquivo externo.")
        for comando in sqlcomandos:
            r = self.db.cursor.execute(comando)
            for c in r.fectchall():
                print(c)
                #Gravando no banco de dados
    self.db.commit_db()


#Alterando os dados

def atualizar(self, id):
    try:
        c = self.localizar_cliente(id)
        if c:
            #solicitando os dados ao usuáRibeiro
            self.novo_fone = input('Fone: ')
            self.db.cursor.execute("""
            UPDATE clientes
            SET fone = ?
            WHERE id = ?
            """, (self.novo_fone, id,))
            #gravando no banco de dadoss
            self.db.commit_db()
            print('Não existe cliente com o id informadp.')
    except e:
            raise e


#Deletando os dados
def deletar(self, id):
    try:
        c = self.localizar_cliente(id)  #verificando se exista cliente com id passado, caso exista
        if c:
            self.db.cursor.execute("""
            DELETE FROM clientes WHERE id = ?
            """, (id,))
            self.db.commit_db()
            print("Registro %d excluido com sucesso." % id)
        else:
            print ('Não existe cliente com o código informado.')
    except e:
        raise e
