import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './components/Home';
import Analyzer from './components/Analyzer';
import './App.css';

// These are placeholder components that you can implement later
const Dashboard = () => <div className="container">Dashboard Coming Soon</div>;
const AdminPanel = () => <div className="container">Admin Panel Coming Soon</div>;
const Login = () => <div className="container">Login Page Coming Soon</div>;

function App() {
  return (
    <Router>
      <div className="app">
        <Navbar />
        <div className="main-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/analyzer" element={<Analyzer />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/admin" element={<AdminPanel />} />
            <Route path="/login" element={<Login />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;