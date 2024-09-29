import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { getUsers, deleteUser, updateUser, addUser } from '../api/AdmApi';
import { updateTask, deleteTask , getTasks} from '../api/TaskApi'; 
import './AdminPage.css';
import logo from '../assets/logo.png';

const AdminPage = () => {
  const [users, setUsers] = useState([]);
  const [tasks, setTasks] = useState([]);
  const navigate = useNavigate();
  const [editingUserId, setEditingUserId] = useState(null);
  const [updatedUserData, setUpdatedUserData] = useState({ username: '', email: '' });
  const [editingTaskId, setEditingTaskId] = useState(null);
  const [updatedTaskData, setUpdatedTaskData] = useState({ title: '', status: '' });
  const [newUsername, setNewUsername] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [newEmail, setNewEmail] = useState('');


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

  const handleLogoClick = () => {
    navigate('/');
  };


  // crud do usuário 
  const handleDeleteUser = async (userId) => {
    await deleteUser(userId);
    setUsers(users.filter(user => user.id !== userId));
  };

  const handleAddUser = async () => {
    if (newUsername.trim() && newPassword.trim() && newEmail.trim()) {
      try {
        const user = await addUser({
          username: newUsername,
          password: newPassword,
          email: newEmail,
        });

        console.log('Usuário adicionado:', user);
        if (user && user.username) {
          setUsers([...users, user]);
          setNewUsername('');
          setNewPassword('');
          setNewEmail('');
        } else {
          console.error('Usuário não válido recebido da API:', user);
        }
      } catch (error) {
        console.error('Erro ao adicionar usuário:', error);
      }
    } else {
      console.error('Preencha todos os campos.');
    }
  };
  

  // crud das tasks 
  const handleDeleteTask = async (taskId) => {
    try {
      await deleteTask(taskId);
      setTasks(tasks.filter(task => task.id !== taskId));
    } catch (error) {
      console.error('Erro ao excluir tarefa:', error);
    }
  };

  const handleUpdateTask = async (taskId) => {
    const task = tasks.find(task => task.id === taskId);
    
    if (!task) {
      console.error('Tarefa não encontrada');
      return;
    }
    
    const taskData = {
      title: updatedTaskData.title || task.title,
      status: updatedTaskData.status || task.status,
      description: task.description,
      due_date: task.due_date,
      user_id : task.user_id,
      create_at: task.create_at || '',
    };
  
    try {
      await updateTask(taskId, taskData);
    
      setTasks(prevTasks => prevTasks.map(task => 
        task.id === taskId ? { ...task, ...taskData } : task
      ));
      setEditingTaskId(null);
    } catch (error) {
      console.error('Erro ao atualizar tarefa:', error);
    }
  };

  const handleUpdateUser = async (id) => {
    const user = users.find(user => user.id === id);
    const userData = {
      username: updatedUserData.username,
      email: updatedUserData.email,
      password: user.password,
    };

    try {
      await updateUser(id, userData);
      setUsers(prevUsers => prevUsers.map(user => 
        user.id === id ? { ...user, ...userData } : user
      ));
      setEditingUserId(null);
    } catch (error) {
      console.error('Erro ao atualizar usuário:', error);
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


      

        <section className="add-user-section">
            <h2>Cadastrar Novo Usuário</h2>
            <div className="user-input">
              <input
                type="text"
                value={newUsername}
                onChange={(e) => setNewUsername(e.target.value)}
                placeholder="Nome de usuário..."
              />
              <input
                type="email"
                value={newEmail}
                onChange={(e) => setNewEmail(e.target.value)}
                placeholder="Email..."
              />
              <input
                type="password"
                value={newPassword}
                onChange={(e) => setNewPassword(e.target.value)}
                placeholder="Senha..."
              />
              <button className="add-user-button" onClick={handleAddUser}>
                Adicionar
              </button>
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
                    <td>{editingTaskId === task.id ? (
                      <input 
                        type="text" 
                        value={updatedTaskData.title} 
                        onChange={(e) => setUpdatedTaskData({ ...updatedTaskData, title: e.target.value })} 
                      />
                    ) : task.title}</td>
                    <td>{editingTaskId === task.id ? (
                      <select 
                        value={updatedTaskData.status}
                        onChange={(e) => setUpdatedTaskData({ ...updatedTaskData, status: e.target.value })}>
                        <option value="em aberto">Em Aberto</option>
                        <option value="em andamento">Em andamento</option>
                        <option value="concluída">Concluída</option>
                      </select>
                    ) : task.status}</td>
                    <td>
                      {editingTaskId === task.id ? (
                        <>
                          <button className="save-button" onClick={() => handleUpdateTask(task.id)}>Salvar</button>
                          <button className="cancel-button" onClick={() => setEditingTaskId(null)}>Cancelar</button>
                        </>
                      ) : (
                        <>
                          <button className="edit-button" onClick={() => {
                            setEditingTaskId(task.id);
                            setUpdatedTaskData({ title: task.title, status: task.status });
                          }}>Editar</button>
                          <button className="delete-button" onClick={() => handleDeleteTask(task.id)}>Excluir</button>
                        </>
                      )}
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
};

export default AdminPage;