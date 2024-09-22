import React, { useState } from 'react';
import './TaskEdit.css'; // Certifique-se de que o arquivo CSS está no mesmo diretório

const TaskEdit = ({ task, onClose, onSave }) => {
  const [title, setTitle] = useState(task.title);
  const [description, setDescription] = useState(task.description);
  const [dueDate, setDueDate] = useState(task.due_date);
  const [status, setStatus] = useState(task.status);

  const handleSave = () => {
    const updatedTask = {
      ...task,
      title,
      description,
      due_date: dueDate,
      status,
    };
    onSave(updatedTask); // Chama a função de callback para salvar a task
    onClose(); // Fecha a tela de edição
  };

  return (
    <div className="task-edit-modal">
      <h2>Edit Task</h2>
      <form onSubmit={(e) => e.preventDefault()}>
        <label>
          Title:
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </label>
        <label>
          Description:
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        </label>
        <label>
          Due Date:
          <input
            type="datetime-local"
            value={new Date(dueDate).toISOString().substring(0, 16)}
            onChange={(e) => setDueDate(e.target.value)}
          />
        </label>
        <label>
          Status:
          <select
            value={status}
            onChange={(e) => setStatus(e.target.value)}
          >
            <option value="em aberto">Em Aberto</option>
            <option value="concluída">Concluída</option>
            <option value="cancelada">Cancelada</option>
          </select>
        </label>
        <div className="button-group">
          <button type="button" onClick={handleSave}>
            Save
          </button>
          <button type="button" onClick={onClose}>
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
};

export default TaskEdit;
