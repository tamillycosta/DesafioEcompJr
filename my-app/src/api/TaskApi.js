const API_URL = 'http://localhost:8000/api/v1/';

// Função para obter tarefas
export const getTasks = async () => {
    const response = await fetch(`http://localhost:8000/api/v1/task-list`);
    // Adicione isso no início do componente

    return response.json();
  };


export const getTask = async (title) => {
    const response = await fetch(`http://localhost:8000/api/v1/task${title}`);
    // Adicione isso no início do componente

    return response.json();
};


export const getUserTask = async (userId) => {
  try {
    const response = await fetch(`http://localhost:8000/api/v1/get-user-tasks/${userId}`);

    if (!response.ok) {
      const errorDetails = await response.json();
      throw new Error(errorDetails.detail || 'Erro ao buscar tarefas do usuário');
    }

    const tasks = await response.json();
    return tasks;  // Retorna a lista de tarefas do usuário
  } catch (error) {
    console.error("Erro ao buscar tarefas")
    }
  }

// Função para adicionar uma tarefa
export const addTask = async (task) => {
    const response = await fetch(`http://localhost:8000/api/v1/task-create`, {
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
    const response = await fetch(`http://localhost:8000/api/v1/task-delete/${taskId}`, {
      method: 'DELETE',
    });
    return response.json();
  };
  



 export const updateTask = async (id, taskData) => {
    try { 
      const response = await fetch(`http://localhost:8000/api/v1/task-update/${id}/`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(taskData),
  
      });
  
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(`Erro: ${errorData.message || 'Erro desconhecido'}`);
      }
  
      return await response.json();
    } catch (error) {
      console.error('Erro ao atualizar tarefa:', error.response?.data || error.message);
  }
   
  };
  
