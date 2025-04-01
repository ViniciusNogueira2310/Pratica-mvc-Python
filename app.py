from flask import Flask, render_template, request, redirect, url_for
from model.tarefa import Tarefa

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        id_tarefa = request.form.get('id_tarefa')
        titulo = request.form['titulo']
        data_conclusao = request.form['data_conclusao']
        
        if id_tarefa:  # Se tem ID, é uma edição
            tarefa = Tarefa(titulo=titulo, data_conclusao=data_conclusao, id=id_tarefa)
        else:  # Se não tem ID, é uma nova tarefa
            tarefa = Tarefa(titulo=titulo, data_conclusao=data_conclusao)
            
        tarefa.salvarTarefa()
        return redirect(url_for('index'))

    tarefas = Tarefa.listarTarefas()
    return render_template('index.html', tarefas=tarefas, title='Minhas Tarefas')

@app.route('/edit/<int:id>', methods=['GET'])
def edit(id):
    tarefa = Tarefa.buscarTarefaPorId(id)
    tarefas = Tarefa.listarTarefas()
    return render_template('index.html', tarefa_edicao=tarefa, tarefas=tarefas, title='Editar Tarefa')

@app.route('/delete/<int:id>')
def delete(id):
    Tarefa.apagarTarefa(id)
    return redirect(url_for('index'))