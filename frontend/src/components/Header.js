import React from 'react';
import '../styles/Header.css';

const Header = () => {
  return (
    <header className="header">
      <h1>Demand Prediction Dashboard</h1>
      <p>Upload your data file to see the demand predictions for Bonniplast.</p>
    </header>
  );
};

export default Header;
