import React, { useState } from 'react';
import { loginUser } from '../api/api';
import { useNavigate } from 'react-router-dom';
import './LoginPage.css';

const LoginPage = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await loginUser({ username, password });

      if (response) {
        // Redirecionar para a página de tarefas se o login for bem-sucedido
        navigate('/tasks'); // redirecione para a página correta
      } else {
        setError('Não foi possível autenticar. Por favor, tente novamente.');
      }
    } catch (error) {
      console.error('Erro ao fazer login:', error);
      setError('Ocorreu um erro no login. Tente novamente.');
    }
  };

  return (
    <div className="login-page">
      <div className="login-form-container">
        <h2 className="login-title">Bem-vindo de volta!</h2>
        <form onSubmit={handleLogin} className="login-form">
          <div className="form-group">
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="Seu username"
              required
              className="login-input"
            />
          </div>
          <div className="form-group">
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Sua senha"
              required
              className="login-input"
            />
          </div>
          <button type="submit" className="login-btn">Entrar</button>
        </form>
        {error && <p className="error-message">{error}</p>}

        <div className="signup-links-container">
          <p className="signup-link">
            Não tem uma conta? <a href="/register">Cadastre-se</a>
          </p>
          <p className="signup-link">
            Entrar como Adm? <a href="/login-admin">Logar como Adm</a>
          </p>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
