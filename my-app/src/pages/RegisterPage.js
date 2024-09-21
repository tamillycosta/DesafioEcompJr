import React, { useState } from 'react';
import './RegisterPage.css';
import { registerUser } from '../api/api';
import { useNavigate } from 'react-router-dom'; // Importa o hook useNavigate

const RegisterPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [username, setUsername] = useState('');
  const [error, setError] = useState(null); // Estado para armazenar erros
  const navigate = useNavigate(); // Hook para redirecionamento

  const handleRegister = async (e) => { // Torna a função assíncrona
    e.preventDefault();
    try {
      // Corrige a chamada da função registerUser com os parâmetros corretos
      const response = await registerUser({ username, password, email });

      if (response && response.success) {
        navigate('/login');
      } else {
        setError('Não foi possível registrar. Por favor, tente novamente.');
      }
    } catch (error) {
      console.error('Erro ao fazer registro:', error);
      setError('Ocorreu um erro no registro. Tente novamente.');
    }
  };

  return (
    <div className="register-page">
      <div className="register-form-container">
        <h2 className="register-title">Crie sua conta</h2>
        <form onSubmit={handleRegister} className="register-form">
          <div className="form-group">
            <input 
              type="text" // Tipo corrigido
              value={username} 
              onChange={(e) => setUsername(e.target.value)} 
              placeholder="Seu Username" 
              required 
              className="register-input" 
            />
          </div>
          <div className="form-group">
            <input 
              type="email" // Tipo corrigido
              value={email} 
              onChange={(e) => setEmail(e.target.value)} 
              placeholder="Seu email" 
              required 
              className="register-input" 
            />
          </div>
          <div className="form-group">
            <input 
              type="password" 
              value={password} 
              onChange={(e) => setPassword(e.target.value)} 
              placeholder="Sua senha" 
              required 
              className="register-input" 
            />
          </div>
          <button type="submit" className="register-btn">Registrar-se</button>
        </form>
        {error && <p className="error-message" style={{ color: 'red' }}>{error}</p>} {/* Exibe mensagens de erro */}
        <p className="login-link">Já tem uma conta? <a href="/login">Entrar</a></p>
      </div>
    </div>
  );
};

export default RegisterPage;
