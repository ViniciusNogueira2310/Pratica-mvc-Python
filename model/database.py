import mysql.connector as mc# Esta é a biblioteca do conector do MySQL
from mysql.connector import Error # Importanto a classe Error (para tratar as mensagens de erro do código)
from dotenv import load_dotenv # Importando a função load_dotenv
from os import getenv # Importando a função getenv

class Database: #Declarando variaveis para a class
    def __init__(self):  #metodo construtor é iniciado assim que a classe é inicializada
        load_dotenv()
        self.host = getenv('DB_HOST')
        self.username = getenv('DB_USER')
        self.password = getenv('DB_PSWD')
        self.database = getenv('DB_NAME')
        self.connection = None # Inicialização da conexão
        self.cursor = None # Inicialização do cursor

    def conectar(self):
        """Estabele uma conexão com o banco de dados."""#docstring
        try:
            self.connection = mc.connect( #self é necessário, connect é um metodo
                host = self.host,
                database = self.database,
                user = self.username,
                password = self.password
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                print('Conexão ao banco de dados realizada com sucesso!')

        except Error as e:
            print(f'Erro de conexão: {e}')
            self.connection = None
            self.cursot = None

    def desconectar(self):
        """Encerra a conexão com o banco de dados e o cursor, se
        existirem."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print('Conexão com o banco de dados encerrada com sucesso!')

    def executar(self, sql, params=None): #para ninguem deletar 
        """Executa uma instrução no banco de dados."""
        if self.connection is None and self.cursor is None:
            print('Conexão ao banco de dados não estabelecida!')
            return None
        
        try:
            self.cursor.execute(sql, params)
            self.connection.commit()
            return self.cursor #o curso é um tipo de mensageiro (se ele foi, ele voltou com algo)
        except Error as e:
            print(f'Erro de execução: {e}')
            return None
        

    def consultar(self, sql, params=None):
        """Executa uma consulta no banco de dados."""
        if self.connection is None and self.cursor is None:
            print('Conexão ao banco de dados não estabelecida!')
            return None
        
        try:
            self.cursor.execute(sql, params)
            #self.connection.commit() -> select não usa commit
            return self.cursor.fetchall()
        except Error as e:
            print(f'Erro de consulta: {e}')
            return None
        

# Area 51
db = Database()
db.conectar()
#db.executar('insert into tarefa (titulo) values ("Teste de tarefa")')
print(db.consultar('select * from tarefa'))
db.desconectar()