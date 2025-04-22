import React, { useEffect, useState } from 'react';
import api from '../api/api';
import JobCard from './JobCard';
import JobForm from './JobForm';

const JobList = () => {
  const [jobs, setJobs] = useState([]);
  const [jobToEdit, setJobToEdit] = useState(null);

  const fetchJobs = async () => {
    const response = await api.get('/applications/jobs');
    setJobs(response.data);
  };

  const handleAddOrUpdateJob = async (job) => {
    if (job.id) {
      await api.put(`/applications/jobs/${job.id}`, job);
    } else {
      await api.post('/applications/jobs', job);
    }
    fetchJobs();
    setJobToEdit(null);
  };

  const handleDelete = async (id) => {
    await api.delete(`/applications/jobs/${id}`);
    fetchJobs();
  };

  const handleEdit = (job) => {
    setJobToEdit(job);
  };

  useEffect(() => {
    fetchJobs();
  }, []);

  return (
    <div className="container" style={{ display: 'flex', justifyContent: 'space-between' }}>
      <div className="job-list" style={{ width: '60%' }}>
        <h2>My Job Applications</h2>
        {jobs.map((job) => (
          <JobCard key={job.id} job={job} onDelete={handleDelete} onEdit={handleEdit} />
        ))}
      </div>

      <div className="job-form" style={{ width: '35%' }}>
        <h2>Add Job Application</h2>
        <JobForm onSubmit={handleAddOrUpdateJob} jobToEdit={jobToEdit} />
      </div>
    </div>
  );
};

export default JobList;
