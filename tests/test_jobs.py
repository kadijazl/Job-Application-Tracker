from fastapi.testclient import TestClient
from app.main import app 

client = TestClient(app)

def test_get_jobs():
    response = client.get("/applications/jobs/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_job():
    # Test valid job creation
    job_data = {
        "company_name": "Air Asia",
        "job_title": "Data Analyst",
        "application_date": "2025-04-18",
        "status": "Applied"
    }
    response = client.post("/applications/jobs/", json=job_data)
    assert response.status_code == 200
    assert response.json()["company_name"] == job_data["company_name"]
    assert response.json()["job_title"] == job_data["job_title"]
    assert response.json()["application_date"] == job_data["application_date"]
    assert response.json()["status"] == "Applied"

def test_update_job():
    # First, create a job to update
    job_data = {
        "company_name": "Tesla",
        "job_title": "Software Engineer",
        "application_date": "2025-04-19",
        "status": "Applied"
    }
    create_response = client.post("/applications/jobs/", json=job_data)
    job_id = create_response.json()["id"]
    
    # Now, update the job with all the details
    updated_job_data = {
        "company_name": "Tesla",
        "job_title": "Senior Software Engineer",  # Updated job title
        "application_date": "2025-04-22",       # Updated application date
        "status": "Interviewing"                 # Updated status
    }
    
    response = client.put(f"/applications/jobs/{job_id}", json=updated_job_data)
    assert response.status_code == 200
    assert response.json()["company_name"] == updated_job_data["company_name"]
    assert response.json()["job_title"] == updated_job_data["job_title"]
    assert response.json()["application_date"] == updated_job_data["application_date"]
    assert response.json()["status"] == updated_job_data["status"]

def test_delete_job():
    # First, create a job to delete
    job_data = {
        "company_name": "Google",
        "job_title": "Data Scientist",
        "application_date": "2025-04-20",
        "status": "Applied"
    }
    create_response = client.post("/applications/jobs/", json=job_data)
    job_id = create_response.json()["id"]
    
    # Now, delete the job
    response = client.delete(f"/applications/jobs/{job_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Job application deleted"}


def test_update_invalid_job_status():
    # Trying to update a non-existent job
    job_data = {
        "company_name": "Nonexistent Company",
        "job_title": "Nonexistent Job",
        "application_date": "2025-04-18",
        "status": "Applied"
    }
    response = client.put("/applications/jobs/999999", json=job_data)  # Use body instead of query
    assert response.status_code == 404  # Now expecting 404, as the job doesn't exist
    assert response.json() == {"detail": "Job not found"}

def test_create_job_invalid_data():
    # Test creating a job with invalid data (e.g., missing company_name)
    invalid_data = {
        "job_title": "Data Analyst",
        "application_date": "2025-04-18",
        "description": "-"
    }
    response = client.post("/applications/jobs/", json=invalid_data)
    assert response.status_code == 422
    assert "company_name" in response.json()["detail"][0]["loc"]
