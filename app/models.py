from sqlalchemy import Column, Integer, String, Date
from .database import Base

class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, index=True)
    job_title = Column(String)
    application_date = Column(Date)
    status = Column(String, default="Applied")

   