import React, { useState, useEffect } from 'react';
import { addTask, deleteTask, updateTask, getUserTask } from '../api/TaskApi';
import './TaskPage.css';
import logo from '../assets/logo.png';

const TaskPage = () => {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState('');
  const [newTaskStatus, setNewTaskStatus] = useState('em aberto');
  const [newTaskDuration, setNewTaskDuration] = useState('');
  const [searchTerm, setSearchTerm] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [editingTaskId, setEditingTaskId] = useState(null);
  const [updatedTaskData, setUpdatedTaskData] = useState({ title: '', status: '' });

  useEffect(() => {
    const fetchTasks = async () => {
      setLoading(true);
      const user = JSON.parse(localStorage.getItem('user'));

      if (!user || !user.id) {
        console.error("Usuário não encontrado no localStorage.");
        setError("Usuário não encontrado.");
        setLoading(false);
        return;
      }

      try {
        const data = await getUserTask(user.id);
        console.log('Tarefas recebidas:', data);
        setTasks(data || []);
      } catch (error) {
        console.error('Erro ao buscar tarefas:', error);
        setError('Erro ao carregar tarefas.');
      } finally {
        setLoading(false);
      }
    };

    fetchTasks();
  }, []);



  const handleAddTask = async () => {
    const user = JSON.parse(localStorage.getItem('user'));
  
    if (!user || !user.id) {
      console.error("Usuário não encontrado no localStorage.");
      return;
    }
  
    const userId = user.id;
    const currentDateTime = new Date().toISOString();
  
    if (newTask.trim() && newTaskDuration.trim()) {
      try {
        const task = await addTask({
          title: newTask,
          status: newTaskStatus,
          description: '',
          due_date: newTaskDuration,
          create_at: currentDateTime,
          user_id: userId
        });
  
        console.log('Tarefa adicionada:', task);
        if (task && task.title) {
          setTasks((prevTasks) => [...prevTasks, task]); // Adiciona a nova tarefa ao estado
          setNewTask('');
          setNewTaskStatus('em aberto');
          setNewTaskDuration('');
        } else {
          console.error('Tarefa não válida recebida da API:', task);
        }
      } catch (error) {
        console.error('Erro ao adicionar tarefa:', error);
      }
    }
  };
  
  const handleDeleteTask = (id) => {
    deleteTask(id)
      .then(() => setTasks(tasks.filter((task) => task.id !== id)))
      .catch((error) => console.error('Erro ao excluir tarefa:', error));
  };

  const handleUpdateTask = async (taskId) => {
    const task = tasks.find(task => task.id === taskId);

    if (!task) {
      console.error('Tarefa não encontrada');
      return;
    }

    const taskData = {
      title: updatedTaskData.title || task.title,
      status: updatedTaskData.status || task.status,
      description: task.description,
      due_date: task.due_date,
      user_id : task.user_id,
      create_at: task.create_at || '',
    };

    console.log("Enviando dados para atualização da tarefa:", taskData);

    try {
      await updateTask(taskId, taskData);
      setTasks(prevTasks => prevTasks.map(task => 
        task.id === taskId ? { ...task, ...taskData } : task
      ));
      setEditingTaskId(null);
      setUpdatedTaskData({ title: '', status: '' });
    } catch (error) {
      console.error('Erro ao atualizar tarefa:', error);
    }
  };

  const filteredTasks = tasks.filter(task => 
    task.title && task.title.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="task-page">
      <div className="logo-container" onClick={() => window.location.href = '/'}>
        <img src={logo} alt="EcompJr Logo" className="logo" />
      </div>
      <div className="main-content">
        <h1>Gerenciar Tarefas</h1>
        {loading && <p>Carregando tarefas...</p>}
        {error && <p>{error}</p>}
        
        <div className="task-search">
          <input
            type="text"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder="Buscar Tarefa"
          />
        </div>

        <section className="add-task-section">
          <h2>Cadastrar Nova Tarefa</h2>
          <div className="task-input">
            <input
              type="text"
              value={newTask}
              onChange={(e) => setNewTask(e.target.value)}
              placeholder="Título da tarefa..."
            />
            <select
              value={newTaskStatus}
              onChange={(e) => setNewTaskStatus(e.target.value)}>
              <option value="em aberto">Em Aberto</option>
              <option value="em andamento">Em andamento</option>
            </select>
            <input
              type="date"
              value={newTaskDuration}
              onChange={(e) => setNewTaskDuration(e.target.value)}
            />
            <button className="add-task-button" onClick={handleAddTask}>
              Adicionar
            </button>
          </div>
        </section>

        <section id="tasks" className="tasks-section">
          <h2>Lista de Tarefas</h2>
          <div className="table-container">
            <table className="admin-table">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Título</th>
                  <th>Status</th>
                  <th>Cumprir até</th>
                  <th>Ações</th>
                </tr>
              </thead>
              <tbody>
                {filteredTasks.map(task => (
                  <tr key={task.id}>
                    <td>{task.id}</td>
                    <td>{editingTaskId === task.id ? (
                      <input 
                        type="text" 
                        value={updatedTaskData.title} 
                        onChange={(e) => setUpdatedTaskData({ ...updatedTaskData, title: e.target.value })} 
                      />
                    ) : task.title}</td>
                    <td>{editingTaskId === task.id ? (
                      <select 
                        value={updatedTaskData.status} 
                        onChange={(e) => setUpdatedTaskData({ ...updatedTaskData, status: e.target.value })}>
                        <option value="em aberto">Em Aberto</option>
                        <option value="concluída">Concluída</option>
                        <option value="em andamento">Em andamento</option>
                      </select>
                    ) : task.status}</td>
                    <td>{task.due_date}</td>
                    <td>
                      {editingTaskId === task.id ? (
                        <>
                          <button className="save-button" onClick={() => handleUpdateTask(task.id)}>Salvar</button>
                          <button className="cancel-button" onClick={() => setEditingTaskId(null)}>Cancelar</button>
                        </>
                      ) : (
                        <>
                          <button className="edit-button" onClick={() => {
                            setEditingTaskId(task.id);
                            setUpdatedTaskData({ title: task.title, status: task.status });
                          }}>Editar</button>
                          <button className="delete-button" onClick={() => handleDeleteTask(task.id)}>Excluir</button>
                        </>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      </div>
    </div>
  );
};

export default TaskPage;
