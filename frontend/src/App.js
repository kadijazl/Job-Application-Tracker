import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import JobList from './components/JobList';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <header>
          <h1>📋 Job Application Tracker</h1>
        </header>

        <main>
          <Routes>
            <Route path="/" element={<JobList />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
