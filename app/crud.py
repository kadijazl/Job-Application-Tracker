from sqlalchemy.orm import Session
from . import models

# Create a new job application
def create_job(db: Session, company_name: str, job_title: str, application_date, status: str):
    db_job = models.JobApplication(company_name=company_name, job_title=job_title, application_date=application_date, status=status)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

# Get all job applications
def get_jobs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.JobApplication).offset(skip).limit(limit).all()

# Update an entire job application
def update_job(db: Session, job_id: int, company_name: str, job_title: str, application_date, status: str):
    db_job = db.query(models.JobApplication).filter(models.JobApplication.id == job_id).first()
    if db_job is None:
        return None
    db_job.company_name = company_name
    db_job.job_title = job_title
    db_job.application_date = application_date
    db_job.status = status
    db.commit()
    db.refresh(db_job)
    return db_job

# Delete a job application
def delete_job(db: Session, job_id: int):
    db_job = db.query(models.JobApplication).filter(models.JobApplication.id == job_id).first()
    if db_job:
        db.delete(db_job)
        db.commit()
        return db_job
    return None
