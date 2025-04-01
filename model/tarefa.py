from model.database import Database

class Tarefa:
    def __init__(self, titulo, id=None, data_conclusao=None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao
        
    def salvarTarefa(self):
        """Salva uma nova tarefa no banco de dados ou atualiza uma existente."""
        db = Database()
        db.conectar()

        if self.id:
            # Se tem ID, é uma atualização
            sql = 'UPDATE tarefa SET titulo = %s, data_conclusao = %s WHERE id = %s'
            params = (self.titulo, self.data_conclusao, self.id)
        else:
            # Se não tem ID, é uma inserção
            sql = 'INSERT INTO tarefa (titulo, data_conclusao) VALUES (%s, %s)'
            params = (self.titulo, self.data_conclusao)
            
        db.executar(sql, params)
        db.desconectar()
    
    @staticmethod
    def buscarTarefaPorId(idTarefa):
        """Busca uma tarefa específica pelo ID."""
        db = Database()
        db.conectar()

        sql = 'SELECT id, titulo, data_conclusao FROM tarefa WHERE id = %s'
        tarefa = db.consultar(sql, (idTarefa,))
        db.desconectar()
        
        if tarefa and len(tarefa) > 0:
            return Tarefa(
                id=tarefa[0]['id'],
                titulo=tarefa[0]['titulo'],
                data_conclusao=tarefa[0]['data_conclusao']
            )
        return None
    
    @staticmethod
    def listarTarefas():
        """Retornar uma lista com todas as tarefas cadastradas."""
        db = Database()
        db.conectar()

        sql = 'SELECT id, titulo, data_conclusao FROM tarefa'
        tarefas = db.consultar(sql)
        db.desconectar()
        return tarefas if tarefas else []
    
    @staticmethod
    def apagarTarefa(idTarefa):
        """Apagar uma tarefa cadastrada no banco de dados."""
        db = Database()
        db.conectar()

        sql = 'DELETE FROM tarefa WHERE id = %s'
        params = (idTarefa,) # Precisa passar a tupla? (a, b, c, ...) SIM! (por isso temos a virgula no final = tupla)

        db.executar(sql, params)
        db.desconectar()