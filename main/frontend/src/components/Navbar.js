import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css'; // Make sure to create a corresponding CSS file for styling

function Navbar() {
  const [isDropdownOpen, setDropdownOpen] = useState(false);

  const toggleDropdown = () => setDropdownOpen(!isDropdownOpen);

  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <Link to="/">CryptoDash</Link>
      </div>
      <ul className="nav-links">
        <li className="nav-item">
          <Link to="/" className="nav-link">Home</Link>
        </li>
        {/* Dropdown for Markets */}
        <li className="nav-item dropdown">
          <span className="nav-link dropdown-toggle" onClick={toggleDropdown}>
            Markets
          </span>
          {isDropdownOpen && (
            <div className="dropdown-menu">
              <Link to="/markets/bitcoin" className="dropdown-item">Bitcoin</Link>
              <Link to="/markets/ethereum" className="dropdown-item">Ethereum</Link>
              {/* Add more market links */}
            </div>
          )}
        </li>
        {/* Additional links */}
        <li className="nav-item">
          <Link to="/about" className="nav-link">About</Link>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
