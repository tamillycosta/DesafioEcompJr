const API_URL = 'http://localhost:8000/api/v1/'; // URL do back-end



export const loginUser = async (credentials) => {
  try {
    const { username, password } = credentials;
    const response = await fetch(`http://localhost:8000/api/v1/login?username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(credentials),
    });

    if (!response.ok) {
      const errorDetails = await response.json();
      throw new Error(errorDetails.detail || 'Login falhou');
    }

    return response.json();
  } catch (error) {
    console.error('Erro ao fazer login:', error);
    throw error;
  }
};



export const loginADM = async (credentials) => {
  try {
    const { username, password } = credentials;
    const response = await fetch(`http://localhost:8000/api/v1/login-adm?username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(credentials),
    });

    if (!response.ok) {
      const errorDetails = await response.json();
      throw new Error(errorDetails.detail || 'Login falhou');
    }

    return response.json();
  } catch (error) {
    console.error('Erro ao fazer login:', error);
    throw error;
  }
};


// Função para excluir um usuário
export const deleteUser = async (userId) => {
  const response = await fetch(`http://localhost:8000/api/v1/adm/delete-user${userId}`, {
    method: 'DELETE',
  });
  return response.ok; // Retorna true se a exclusão foi bem-sucedida
};



// Exemplo de função updateUser em api.js


export const updateUser = async (userId, userData) => {
  try { 
    const response = await fetch(`http://localhost:8000/api/v1/adm/edit-user/${userId}/`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userData),
    });
    

    if (!response.ok) {
      const errorData = await response.json(); // Verifique os dados de erro que a API está retornando
      throw new Error(`Erro ao atualizar usuário: ${JSON.stringify(errorData)}`);
    }

    return await response.json();
  } catch (error) {
    console.error("Erro na API:", error.message);
    throw error;
  }
};






// Função para registrar um usuário
export const registerUser = async (user) => {
  try {
    const response = await fetch('http://localhost:8000/api/v1/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(user),
    });

    if (!response.ok) {
      throw new Error('Registration failed');
    }

    return response.json(); // Retorna a resposta JSON
  } catch (error) {
    console.error('Error during registration:', error);
    throw error;
  }
};


export const registerAdm = async (user) => {
  try {
    const response = await fetch('http://localhost:8000/api/v1/adm/create-account', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(user),
    });

    if (!response.ok) {
      throw new Error('Registration failed');
    }

    return response.json(); // Retorna a resposta JSON
  } catch (error) {
    console.error('Error during registration:', error);
    throw error;
  }
};



// Função para obter tarefas
export const getTasks = async () => {
  const response = await fetch(`http://localhost:8000/api/v1/task-list`);
  return response.json();
};

// Função para obter tarefas
export const getUsers = async () => {
  const response = await fetch(`http://localhost:8000/api/v1/adm-list-users`);
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
