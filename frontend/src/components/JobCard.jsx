import React from 'react';

const JobCard = ({ job, onDelete, onEdit }) => {
  return (
    <div className="job-card">
      <h3>{job.job_title} at {job.company_name}</h3>
      <p><strong>Application Date:</strong> {job.application_date}</p>
      <p><strong>Status:</strong> {job.status}</p>
      <button onClick={() => onEdit(job)}>Edit</button>
      <button onClick={() => onDelete(job.id)}>Delete</button>
    </div>
  );
};

export default JobCard;
