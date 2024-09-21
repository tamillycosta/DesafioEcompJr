
import React, { useState, useEffect } from 'react';


const EditUser = ({ userId, onUpdate, fetchUser }) => {
  const [userData, setUserData] = useState({ username: '', password: '', email: '' });

  useEffect(() => {
    const loadUserData = async () => {
      const data = await fetchUser(userId);
      setUserData(data);
    };

    loadUserData();
  }, [userId, fetchUser]);

  const handleChange = (e) => {
    setUserData({ ...userData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await onUpdate(userId, userData); 
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Nome de Usuário:</label>
        <input type="text" name="username" value={userData.username} onChange={handleChange} required />
      </div>
      <div>
        <label>Senha:</label>
        <input type="password" name="password" value={userData.password} onChange={handleChange} required />
      </div>
      <div>
        <label>Email:</label>
        <input type="email" name="email" value={userData.email} onChange={handleChange} required />
      </div>
      <button type="submit">Atualizar</button>
    </form>
  );
};

export default EditUser;
