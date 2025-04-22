import React, { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { BiCameraMovie, BiMenu, BiX } from 'react-icons/bi';
import './Navbar.css';

const Navbar = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const location = useLocation();

  // Handle scroll event to add shadow to navbar
  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 20) {
        setScrolled(true);
      } else {
        setScrolled(false);
      }
    };

    window.addEventListener('scroll', handleScroll);
    
    // Clean up event listener
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  // Toggle mobile menu
  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  // Close menu when a link is clicked
  const closeMenu = () => {
    setIsMenuOpen(false);
  };

  // Check if a route is active
  const isActive = (path) => {
    return location.pathname === path;
  };

  return (
    <nav className={`navbar ${scrolled ? 'scrolled' : ''}`}>
      <div className="navbar-container">
        <Link to="/" className="navbar-logo" onClick={closeMenu}>
          <BiCameraMovie className="logo-icon" />
          <span className="logo-text">Movie<span className="accent">Sentiment</span></span>
        </Link>

        <div className="menu-icon" onClick={toggleMenu}>
          {isMenuOpen ? <BiX /> : <BiMenu />}
        </div>

        <ul className={isMenuOpen ? 'nav-menu active' : 'nav-menu'}>
          <li className="nav-item">
            <Link 
              to="/" 
              className={`nav-link ${isActive('/') ? 'active' : ''}`} 
              onClick={closeMenu}
            >
              Home
            </Link>
          </li>
          
          <li className="nav-item">
            <Link 
              to="/analyzer" 
              className={`nav-link ${isActive('/analyzer') ? 'active' : ''}`} 
              onClick={closeMenu}
            >
              Analyzer
            </Link>
          </li>
          
          <li className="nav-item">
            <Link 
              to="/dashboard" 
              className={`nav-link ${isActive('/dashboard') ? 'active' : ''}`} 
              onClick={closeMenu}
            >
              Dashboard
            </Link>
          </li>
          
          <li className="nav-item">
            <Link 
              to="/admin" 
              className={`nav-link ${isActive('/admin') ? 'active' : ''}`} 
              onClick={closeMenu}
            >
              Admin
            </Link>
          </li>
          
          <li className="nav-item">
            <Link 
              to="/login" 
              className="nav-link login-button" 
              onClick={closeMenu}
            >
              Login
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;