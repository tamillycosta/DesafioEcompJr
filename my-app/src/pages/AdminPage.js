import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { getUsers, getTasks, deleteUser, updateUser } from '../api/api'; // Ajuste o caminho conforme necessário
import './AdminPage.css';
import logo from '../assets/logo.png';

const AdminPage = () => {

  const [users, setUsers] = useState([]);
  const [tasks, setTasks] = useState([]);
  const navigate = useNavigate();
  const [editingUserId, setEditingUserId] = useState(null);
  const [updatedUserData, setUpdatedUserData] = useState({ username: '', email: '' });

  useEffect(() => {
    const fetchData = async () => {
      try {
        const usersData = await getUsers();
        setUsers(usersData);

        const tasksData = await getTasks();
        setTasks(tasksData);
      } catch (error) {
        console.error('Erro ao buscar dados:', error);
      }
    };

    fetchData();
  }, []);

  // Função para redirecionar para a página inicial
  const handleLogoClick = () => {
    navigate('/');
  };

  // Função para excluir um usuário
  const handleDeleteUser = async (userId) => {
    await deleteUser(userId);
    setUsers(users.filter(user => user.id !== userId));
  };

 
  const handleUpdateUser = async (id) => {
    
    const user = users.find(user => user.id === id);
    const userData = {
      username: updatedUserData.username,
      email: updatedUserData.email,
      password:  user.password, // Envia a senha atual se não foi alterada
    };
  
    console.log("Enviando dados para atualização:", userData);
  
    try {
      await updateUser(id, userData);
      setUsers(prevUsers => prevUsers.map(user => 
        user.id === id ? { ...user, ...userData } : user
      ));
      setEditingUserId(null);
    } catch (error) {
      console.error('Erro ao atualizar usuário:', error);
      if (error.response && error.response.data) {
        console.error('Erro da API:', error.response.data);
      } else {
        console.error('Erro desconhecido:', error.message);
      }
    }
  };
  

  
  

  return (
    <div className="admin-page">
      <div className="logo-container">
        <img src={logo} alt="Ecomp Jr Logo" className="logo" onClick={handleLogoClick} />
      </div>

      <aside className="sidebar">
        <h2>Admin</h2>
        <nav>
          <ul>
            <li><a href="#dashboard">Dashboard</a></li>
            <li><a href="#users">Usuários</a></li>
            <li><a href="#tasks">Tarefas</a></li>
          </ul>
        </nav>
      </aside>

      <main className="main-content">
        <section id="dashboard" className="dashboard-section">
          <h2>Dashboard</h2>
          <p>Visão geral das atividades e estatísticas da plataforma.</p>
        </section>

        <section id="users" className="users-section">
          <h2>Gerenciar Usuários</h2>
          <div className="table-container">
            <table className="admin-table">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Nome</th>
                  <th>Email</th>
                  <th>Ações</th>
                </tr>
              </thead>
              <tbody>
                {users.map(user => (
                  <tr key={user.id}>
                    <td>{user.id}</td>
                    <td>{editingUserId === user.id ? (
                      <input 
                        type="text" 
                        value={updatedUserData.username} 
                        onChange={(e) => setUpdatedUserData({ ...updatedUserData, username: e.target.value })} 
                      />
                    ) : user.username}</td>
                    <td>{editingUserId === user.id ? (
                      <input 
                        type="email" 
                        value={updatedUserData.email} 
                        onChange={(e) => setUpdatedUserData({ ...updatedUserData, email: e.target.value })} 
                      />
                    ) : user.email}</td>
                    <td>
                      {editingUserId === user.id ? (
                        <>
                          <button className="save-button" onClick={() => handleUpdateUser(user.id)}>Salvar</button>
                          <button className="cancel-button" onClick={() => setEditingUserId(null)}>Cancelar</button>
                        </>
                      ) : (
                        <>
                          <button className="edit-button" onClick={() => {
                            setEditingUserId(user.id);
                            setUpdatedUserData({ username: user.username, email: user.email });
                          }}>Editar</button>
                          <button className="delete-button" onClick={() => handleDeleteUser(user.id)}>Excluir</button>
                        </>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>

        <section id="tasks" className="tasks-section">
          <h2>Gerenciar Tarefas</h2>
          <div className="table-container">
            <table className="admin-table">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Título</th>
                  <th>Status</th>
                  <th>Ações</th>
                </tr>
              </thead>
              <tbody>
                {tasks.map(task => (
                  <tr key={task.id}>
                    <td>{task.id}</td>
                    <td>{task.title}</td>
                    <td>{task.status}</td>
                    <td>
                      <button className="edit-button">Editar</button>
                      <button className="delete-button">Excluir</button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      </main>
    </div>
  );
}

export default AdminPage;
