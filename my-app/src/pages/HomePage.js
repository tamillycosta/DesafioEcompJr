import React, { useState } from 'react';
import './HomePage.css';

const HomePage = () => {
  const [menuOpen, setMenuOpen] = useState(false);

  const toggleMenu = () => setMenuOpen(!menuOpen);
  
  return (
    <div className="home-page">
      <header>
        {/* Menu hamburger */}
        <div className="menu-toggle" onClick={toggleMenu}>
          <span className={`bar ${menuOpen ? 'open' : ''}`}></span>
          <span className={`bar ${menuOpen ? 'open' : ''}`}></span>
          <span className={`bar ${menuOpen ? 'open' : ''}`}></span>
        </div>
        
        {/* Menu de navegação */}
        <nav className={`nav ${menuOpen ? 'open' : ''}`}>
          <ul>
            <li><a href="/taskpage">Task Page</a></li>
            <li><a href="/register">Register</a></li>
            <li><a href="/login">Login</a></li>
          </ul>
        </nav>
      </header>

      <section className="hero">
        <div className="hero-content">
          <h1>Bem-vindo à Ecomp Jr</h1>
          <p>Gerencie suas tarefas com eficiência e estilo.</p>
          <div className="cta">
            <a href="/register" className="button">Cadastrar</a>
            <a href="/login" className="button">Login</a>
          </div>

          {/* Botão Ver Tarefas logo abaixo dos botões Cadastrar e Login */}
          <div className="tasks-button-container">
            <a href="/taskpage" className="tasks-button">Ver Tarefas</a>
          </div>
        </div>
      </section>

      {/* Seção Sobre Nós abaixo */}
      <section className="about">
        <h2>Sobre Nós</h2>
        <p>A Ecomp Jr está dedicada a oferecer as melhores ferramentas para gerenciamento de tarefas e organização.</p>
      </section>

      {/* Rodapé atualizado */}
      <footer>
        <div className="footer-content">
          {/* Lado esquerdo */}
          <div className="footer-left">
            <h4>Desenvolvido por:</h4>
            <p>Felipe Amorim do Carmo Silva</p>
            {/* Botão GitHub - Felipe */}
            <a href="https://github.com/luffysertao" target="_blank" rel="noopener noreferrer" className="github-button">GitHub - Felipe</a>
            <p>Tamilly Costa Cerqueira</p>
            {/* Botão GitHub - Tamilly */}
            <a href="https://github.com/tamillycosta" target="_blank" rel="noopener noreferrer" className="github-button">GitHub - Tamilly</a>
          </div>

          {/* Lado direito */}
          <div className="footer-right">
            <h4>Localização</h4>
            <p>UEFS - Avenida Transnordestina, s/nº - Módulo 5, MP 51A</p>
            <p>Novo Horizonte, Feira de Santana - BA, 44036-900</p>
            <a href="https://instagram.com/ecompjr" target="_blank" rel="noopener noreferrer" className="instagram-button">Siga no Instagram</a>
            <p>Telefone: (75) 9 8350-2812</p>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default HomePage;
