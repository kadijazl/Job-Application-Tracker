import React, { useState, useEffect } from 'react';

const JobForm = ({ onSubmit, jobToEdit }) => {
  const [job, setJob] = useState({
    id: null,
    company_name: '',
    job_title: '',
    application_date: '',
    status: 'Applied',
  });

  useEffect(() => {
    if (jobToEdit) setJob(jobToEdit);
  }, [jobToEdit]);

  const handleChange = (e) => {
    setJob({ ...job, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(job);
    setJob({
      id: null,
      company_name: '',
      job_title: '',
      application_date: '',
      status: 'Applied',
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="company_name" placeholder="Company Name" value={job.company_name} onChange={handleChange} required />
      <input name="job_title" placeholder="Job Title" value={job.job_title} onChange={handleChange} required />
      <input name="application_date" type="date" value={job.application_date} onChange={handleChange} required />
      <select name="status" value={job.status} onChange={handleChange} required>
        <option value="Applied">Applied</option>
        <option value="Interviewing">Interviewing</option>
        <option value="Offered">Offered</option>
        <option value="Rejected">Rejected</option>
      </select>
      <button type="submit">{jobToEdit ? 'Update' : 'Add'} Job</button>
    </form>
  );
};

export default JobForm;
