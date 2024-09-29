import React, { useState } from 'react';
import { loginADM } from '../api/AdmApi';
import { useNavigate } from 'react-router-dom';
import './AdminLoginPage.css';

const AdminLoginPage = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await loginADM({ username, password });

      if (response && response.success) {
        // Redirecionar para a página de tarefas adm
        navigate('/admin'); 
      } else {
        setError('Não foi possível autenticar. Por favor, tente novamente.');
      }
    } catch (error) {
      console.error('Erro ao fazer login:', error);
      setError('Ocorreu um erro no login. Tente novamente.');
    }
  };

  return (
    <div className="adm-login-page">
    <div className="adm-login-form-container">
      <h2 className="adm-login-title">Bem-vindo de volta!</h2>
      <form onSubmit={handleLogin} className="login-form">
        <div className="form-group">
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            placeholder="Seu username"
            required
            className="adm-login-input"
          />
        </div>
        <div className="form-group">
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Sua senha"
            required
            className="adm-login-input"
          />
        </div>
        <button type="submit" className="adm-login-btn">Entrar</button>
      </form>
      {error && <p className="error-message">{error}</p>}
      <div className="signup-links-container">
        <p className="adm-signup-link">
          Não tem uma conta? <a href="/register-admin">Cadastre-se</a>
        </p>
      </div>
    </div>
  </div>
)}


export default AdminLoginPage;
