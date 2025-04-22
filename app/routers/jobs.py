from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas, database

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/jobs/")
def create_job(job: schemas.JobApplicationCreate, db: Session = Depends(get_db)):
    return crud.create_job(
        db=db,
        company_name=job.company_name,
        job_title=job.job_title,
        application_date=job.application_date,
        status=job.status
    )

@router.get("/jobs/")
def get_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    jobs = crud.get_jobs(db=db, skip=skip, limit=limit)
    return jobs

@router.put("/jobs/{job_id}")
def update_job(job_id: int, job: schemas.JobUpdate, db: Session = Depends(get_db)):
    updated_job = crud.update_job(
        db=db,
        job_id=job_id,
        company_name=job.company_name,
        job_title=job.job_title,
        application_date=job.application_date,
        status=job.status
    )
    if updated_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return updated_job

@router.delete("/jobs/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db)):
    job = crud.delete_job(db=db, job_id=job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return {"message": "Job application deleted"}
