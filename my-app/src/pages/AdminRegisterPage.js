import React, { useState } from 'react';
import './AdminRegisterPage.css';
import { registerAdm } from '../api/api';
import { useNavigate } from 'react-router-dom'; // Importa o hook useNavigate

const RegisterPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [username, setUsername] = useState('');
  const [error, setError] = useState(null); // Estado para armazenar erros
  const navigate = useNavigate(); 

  const handleRegister = async (e) => { // Torna a função assíncrona
    e.preventDefault();
    try {
     
      const response = await registerAdm ({ username, password, email });

      if (response && response.success) {
        navigate('/login-admin');
      } else {
        setError('Não foi possível registrar. Por favor, tente novamente.');
      }
    } catch (error) {
      console.error('Erro ao fazer registro:', error);
      setError('Ocorreu um erro no registro. Tente novamente.');
    }
  };

  return (
    <div className="adm-register-page">
      <div className="adm-register-form-container">
        <h2 className="adm-register-title">Crie sua conta</h2>
        <form onSubmit={handleRegister} className="adm-register-form">
          <div className="adm-form-group">
            <input 
              type="text" // Tipo corrigido
              value={username} 
              onChange={(e) => setUsername(e.target.value)} 
              placeholder="Seu Username" 
              required 
              className="adm-register-input" 
            />
          </div>
          <div className="adm-form-group">
            <input 
              type="email" // Tipo corrigido
              value={email} 
              onChange={(e) => setEmail(e.target.value)} 
              placeholder="Seu email" 
              required 
              className="adm-register-input" 
            />
          </div>
          <div className="adm-form-group">
            <input 
              type="password" 
              value={password} 
              onChange={(e) => setPassword(e.target.value)} 
              placeholder="Sua senha" 
              required 
              className="adm-register-input" 
            />
          </div>
          <button type="submit" className="adm-register-btn">Registrar-se</button>
        </form>
        {error && <p className="error-message" style={{ color: 'red' }}>{error}</p>} {/* Exibe mensagens de erro */}
        <p className="adm-login-link">Já tem uma conta? <a href="/login-admin">Entrar</a></p>
      </div>
    </div>
  );
};

export default RegisterPage;
