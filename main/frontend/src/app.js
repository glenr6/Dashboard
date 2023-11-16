import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import TokenDetail from './components/TokenDetail';
import Navbar from './components/Navbar';
import './app.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar /> {/* Your top navigation bar */}
        <Routes>
          <Route path="/" element={<Dashboard />} /> {/* Main dashboard view */}
          <Route path="/token/:symbol" element={<TokenDetail />} /> {/* Individual token detail view */}
          {/* Add more routes as needed */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;

// TODO: add remaining compontents, server connections, etc. 