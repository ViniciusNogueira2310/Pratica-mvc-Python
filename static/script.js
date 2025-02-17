const tarefaInput = document.getElementById('tarefaInput');
const dataConclusao = document.getElementById('dataConclusao');
const adicionarTarefaButton = document.getElementById('adicionarTarefa');
const listaTarefas = document.getElementById('listaTarefas');
 
function carregarTarefas() {
    const tarefas = JSON.parse(localStorage.getItem('tarefas')) || [];
    listaTarefas.innerHTML = '';
    tarefas.forEach((tarefa, index) => {
        const li = document.createElement('li');
        li.innerHTML = `
            ${tarefa.nome} - Concluir até: ${tarefa.dataConclusao}
            <button onclick="apagarTarefa(${index})">Apagar</button>
        `;
        listaTarefas.appendChild(li);
    });
}
 
function adicionarTarefa() {
    const tarefaNome = tarefaInput.value.trim();
    const data = dataConclusao.value;
 
    if (tarefaNome !== '' && data !== '') {
        const tarefas = JSON.parse(localStorage.getItem('tarefas')) || [];
 
        tarefas.push({ nome: tarefaNome, dataConclusao: data });
 
        localStorage.setItem('tarefas', JSON.stringify(tarefas));
 
        tarefaInput.value = '';
        dataConclusao.value = '';
 
        carregarTarefas();
    } else {
        alert("Por favor, preencha tanto a tarefa quanto a data de conclusão.");
    }
}
 
function apagarTarefa(index) {
    const tarefas = JSON.parse(localStorage.getItem('tarefas')) || [];
    tarefas.splice(index, 1);
 
    localStorage.setItem('tarefas', JSON.stringify(tarefas));
 
    carregarTarefas();
}
 
adicionarTarefaButton.addEventListener('click', adicionarTarefa);
 
window.onload = carregarTarefas;