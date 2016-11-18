import sqlite3

class Connect(object):
    def _init_(self, db_name):
        try:
            #Conectando...
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            #imprimindo nome do banco
            print("Banco:", db_name)
            #lendo a versão do SQLite
            self.cursor.execute('SELECT SQLITE_VERSION()')
            self.data = self.cursor.fetchone()
            #imprimindo a versão do SQLite
            print("SQLite version: %s" % self.data)
        except sqlite3.Error:
            print("Erro ao abrir banco.")
            return False
        def close_db(self):
            if self.conn:
                self.conn.close()
                print("Conexão fechada.")

class ClienteDb(object):
    def _ini_(self):
        self.db = Connect(r'C:\Users\ju\Desktop\esof\clientes.db')
    def close_connection(self):
        self.db.close_db()
if '_name_' == '_main_':
    cliente = ClientesDb()
    cliente.close_connection()
