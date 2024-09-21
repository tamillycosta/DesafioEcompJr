import React, { useState, useEffect } from 'react';
import { getTasks, addTask, deleteTask } from '../api/api'; // Corrigido para getTasks
import './TaskPage.css';
import logo from '../assets/logo.png'; // Caminho para o logo

const TaskPage = () => {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState('');

  useEffect(() => {
    getTasks()
      .then((data) => setTasks(data))
      .catch((error) => console.error('Error fetching tasks:', error));
  }, []);

  const handleAddTask = () => {
    if (newTask.trim()) {
      addTask(newTask)
        .then((task) => setTasks([...tasks, task]))
        .catch((error) => console.error('Error adding task:', error));
      setNewTask('');
    }
  };

  const handleDeleteTask = (id) => {
    deleteTask(id)
      .then(() => setTasks(tasks.filter((task) => task.id !== id)))
      .catch((error) => console.error('Error deleting task:', error));
  };

  return (
    <div className="task-page">
      <div className="logo-container" onClick={() => window.location.href = '/'}>
        <img src={logo} alt="EcompJr Logo" className="logo" />
      </div>
      <div className="main-content">
        <h1>Gerenciar Tarefas</h1>
        <div className="task-input">
          <input
            type="text"
            value={newTask}
            onChange={(e) => setNewTask(e.target.value)}
            placeholder="Nova tarefa..."
          />
          <button className="add-task-button" onClick={handleAddTask}>
            Adicionar
          </button>
        </div>
        <div className="task-list">
          {tasks.map((task) => (
            <div key={task.id} className="task-item">
              <span>{task.name}</span>
              <button className="delete-task-button" onClick={() => handleDeleteTask(task.id)}>
                Excluir
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default TaskPage;
