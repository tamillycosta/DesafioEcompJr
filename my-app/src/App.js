// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import AdminRegisterPage from './pages/AdminRegisterPage';
import TaskPage from './pages/TaskPage';
import AdminPage from './pages/AdminPage';
import AdminLoginPage from './pages/AdminLoginPage';
import TaskEdit from './pages/TaskEdit';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/tasks" element={<TaskPage />} />
        <Route path="/admin" element={<AdminPage />} />
        <Route path="/login-admin" element={<AdminLoginPage />} />
        <Route path="/register-admin" element={<AdminRegisterPage/>} />
        <Route path="/task-edit" element={<TaskEdit/>} />
      </Routes>
    </Router>
  )
}

export default App;