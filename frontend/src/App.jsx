import React from 'react';
import JobList from './components/JobList';
import JobForm from './components/JobForm';

function App() {
  return (
    <div className="app-container">
      <header>
        <h1>📋 Job Application Tracker</h1>
      </header>
      <main className="content">
        <div className="job-list">
          <JobList />
        </div>
        <div className="job-form">
          <JobForm />
        </div>
      </main>
    </div>
  );
}

export default App;
