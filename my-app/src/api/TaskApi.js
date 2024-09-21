const API_URL = 'http://localhost:8000/api/v1/';

// Função para obter tarefas
export const getTasks = async () => {
    const response = await fetch(`http://localhost:8000/api/v1/task-list`);
    return response.json();
  };


// Função para adicionar uma tarefa
export const addTask = async (task) => {
    const response = await fetch(`${API_URL}/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(task),
    });
    return response.json();
  };
  
  
  // Função para excluir uma tarefa
  export const deleteTask = async (taskId) => {
    const response = await fetch(`${API_URL}/tasks/${taskId}`, {
      method: 'DELETE',
    });
    return response.json();
  };
  



export const updateTask = async (id, taskData) => {
    try { 
      const response = await fetch(`http://localhost:8000/api/v1/task-update${id}/`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(taskData),
      });
      
  
      if (!response.ok) {
        const errorData = await response.json(); 
              throw new Error(`Erro ao atualizar usuário: ${JSON.stringify(errorData)}`);
      }
  
      return await response.json();
    } catch (error) {
      console.error("Erro na API:", error.message);
      throw error;
    }
  };
  