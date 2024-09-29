
// Função para um  adm fazer login
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


  // Função para criar uma conta de adm
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



// Função para adicionar uma usuário
export const addUser = async (user) => {
  try {
    const response = await fetch('http://localhost:8000/api/v1/adm/create-user', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(user),
    });

    if (!response.ok) {
      throw new Error('Registration failed');
    }

    return response.json(); 
  } catch (error) {
    console.error('Error during registration:', error);
    throw error;
  }
};




// Função para excluir um usuário
export const deleteUser = async (userId) => {
  const response = await fetch(`http://localhost:8000/api/v1/adm/delete-user${userId}`, {
    method: 'DELETE',
  });
  return response.ok; 
};




// Função para atualizar um usuário
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
      const errorData = await response.json(); 
            throw new Error(`Erro ao atualizar usuário: ${JSON.stringify(errorData)}`);
    }

    return await response.json();
  } catch (error) {
    console.error("Erro na API:", error.message);
    throw error;
  }
};




// Função para obter usuários
export const getUsers = async () => {
  const response = await fetch(`http://localhost:8000/api/v1/adm-list-users`);
  return response.json();
};


export const getUser = async (username) => {
  try {
    const response = await fetch(`http://localhost:8000/api/v1/adm-get/${username}`);
    const userData = await response.json();
    console.log(username)
    return userData.id;  // Retorna o ID do usuário
  } catch (error) {
    console.error("Erro ao buscar ID do usuário:", error);
    return null;
  }
};



