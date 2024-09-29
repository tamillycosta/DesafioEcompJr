


// função para um usuário fazer login
export const loginUser = async (credentials) => {
  try {
    const response = await fetch(`http://localhost:8000/api/v1/login`, {
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

    const userData = await response.json();
    localStorage.setItem('user', JSON.stringify(userData));  // Salvando os dados do usuário
    
    return userData;
  } catch (error) {
    console.error('Erro ao fazer login:', error);
    throw error;
  }
};





// Função para criar conta de um usuário
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





