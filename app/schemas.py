from pydantic import BaseModel
from datetime import date

class JobApplicationCreate(BaseModel):
    company_name: str
    job_title: str
    application_date: date
    status: str

    class Config:
        orm_mode = True 

class JobUpdate(BaseModel):
    company_name: str
    job_title: str
    application_date: date
    status: str
